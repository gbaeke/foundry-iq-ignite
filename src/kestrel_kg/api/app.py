from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from ..config import Settings, get_settings
from ..middleware import RequestContext
from .errors import ApiError, install_handlers
from .lab import router as lab_router

ROOT = Path(__file__).resolve().parents[3]  # the repository: frontend/dist


def create_app(
    settings: Settings | None = None,
) -> FastAPI:
    settings = settings or get_settings()

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        yield

    app = FastAPI(
        title="Kestrel Graph Lab",
        openapi_url="/api/openapi.json",
        docs_url="/api/docs",
        lifespan=lifespan,
        # operation ids are the handlers' names: the generated client gets listNotes(), not listNotesApiNotesGet()
        generate_unique_id_function=lambda route: route.name,
    )
    app.state.settings = settings
    install_handlers(app)
    app.add_middleware(RequestContext)  # added last, so it runs first: every response gets its id and headers

    api = APIRouter(prefix="/api")

    @api.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    api.include_router(lab_router)
    app.include_router(api)
    _serve_frontend(app, ROOT / "frontend" / "dist")
    return app


def _serve_frontend(app: FastAPI, dist: Path) -> None:
    """The built SPA: real files as they are, every other path gets index.html (the router takes it from there)."""
    if not dist.is_dir():
        return  # not built (tests, or `npm run dev` serves it)
    app.mount("/assets", StaticFiles(directory=dist / "assets"), name="assets")

    @app.api_route("/{path:path}", methods=["GET", "HEAD"], include_in_schema=False)
    async def spa(path: str) -> FileResponse:
        if path == "api" or path.startswith("api/"):
            raise ApiError("not_found", f"No API endpoint /{path}", 404)  # never the SPA for a mistyped API call
        file = (dist / path).resolve()
        if path and file.is_file() and file.is_relative_to(dist.resolve()):
            return FileResponse(file)
        return FileResponse(dist / "index.html", headers={"Cache-Control": "no-cache"})
