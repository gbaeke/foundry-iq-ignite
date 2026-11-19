"""Check corpus documents against the ground truth rules in groundtruth/expansion-brief.md.

For every project document it flags:
- Kestrel or DataForge people who aren't on that project's team (Lotte Willems is always allowed)
- technologies named that aren't in that project's technology list
- look-alike name swaps

Usage: uv run python -m kestrel_kg.check_corpus
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from kestrel_kg.client import ROOT

W = yaml.safe_load((ROOT / "groundtruth" / "world.yaml").read_text())
PEOPLE = {p["id"]: p for p in W["people"]}
STAFF = {pid: p["name"] for pid, p in PEOPLE.items() if p["employer"] in ("kestrel", "dataforge")}
ALL_TECH = W["technologies"]
SWAPS = ["Pieter Desmet", "Tine De Smet", "Sofie Wouters", "Jan Claes", "Evelien Wouters", "Ruben Claes"]


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


PROJECTS = {}
for p in W["projects"]:
    s = slug(p["name"])
    PROJECTS[s] = p
    # short slugs used by the original document plan
    PROJECTS[s.replace("scaldis-", "").replace("fortalis-", "")] = p


def mentions(text: str, full_name: str) -> bool:
    first, last = full_name.split()[0], full_name.split()[-1]
    return full_name in text or (re.search(rf"\b{first}\b", text) is not None and last in text)


def check(path: Path) -> list[str]:
    text = path.read_text()
    issues = [f"look-alike swap '{s}'" for s in SWAPS if s in text]
    stem = path.stem.split("_", 2)
    proj = PROJECTS.get(stem[2]) if len(stem) == 3 else None
    if proj is None:
        return issues  # internal or cross-project document: only swap checks apply
    team = set(proj["team"]) | {"lotte"}
    for pid, name in STAFF.items():
        if pid not in team and re.search(rf"\b{re.escape(name)}\b", text):
            issues.append(f"{name} is not on {proj['name']}")
    for tech in ALL_TECH:
        if tech not in proj["technologies"] and re.search(rf"\b{re.escape(tech)}\b", text):
            issues.append(f"technology '{tech}' not used by {proj['name']}")
    return issues


def main() -> None:
    files = sorted((ROOT / "corpus").rglob("*.md"))
    unmatched, bad = [], 0
    for f in files:
        stem = f.stem.split("_", 2)
        if f.parent.name != "kestrel" and (len(stem) < 3 or stem[2] not in PROJECTS):
            unmatched.append(f.relative_to(ROOT))
        for issue in check(f):
            bad += 1
            print(f"{f.relative_to(ROOT)}: {issue}")
    for u in unmatched:
        print(f"{u}: file name doesn't match a project slug")
    print(f"\n{len(files)} files, {bad} issues, {len(unmatched)} unmatched names")


if __name__ == "__main__":
    main()
