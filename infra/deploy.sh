#!/usr/bin/env bash
# Deploys everything the Kestrel knowledge graph demo needs into one resource group.
# Idempotent: safe to re-run.
set -euo pipefail

SUB="${AZURE_SUBSCRIPTION_ID:-$(az account show --query id -o tsv)}"
RG="${RG:-rg-foundry-iq-kg}"
LOC="${LOC:-swedencentral}"
SEARCH="${SEARCH:-srch-kestrel-r1}"
# Microsoft Retriever 1 is only offered in a few regions (Fetch Offerings: westus3, westcentralus,
# northeurope, japaneast); North Europe has no Serverless, so search runs in West US 3.
SEARCH_LOC="${SEARCH_LOC:-westus3}"
STORAGE="${STORAGE:-stkestrelkg$(echo "$SUB" | cut -c1-6)}"
CONTAINER="${CONTAINER:-kestrel-corpus}"
FOUNDRY="${FOUNDRY:-aif-kestrel-kg}"
CHAT_MODEL="gpt-5.6-luna"; CHAT_VERSION="2026-07-09"
EMBED_MODEL="text-embedding-3-small"; EMBED_VERSION="1"
ME="$(az ad signed-in-user show --query id -o tsv)"
SEARCH_API="2026-09-01-Preview"

echo "== resource group"
az group create -n "$RG" -l "$LOC" --tags purpose=foundry-iq-kg-demo -o none

echo "== Foundry IQ Serverless service (management preview API; az search has no serverless sku yet)"
SEARCH_URL="https://management.azure.com/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Search/searchServices/$SEARCH?api-version=$SEARCH_API"
if ! az rest --method get --url "$SEARCH_URL" -o none 2>/dev/null; then
  az rest --method put --url "$SEARCH_URL" \
    --body "{\"location\":\"$SEARCH_LOC\",\"sku\":{\"name\":\"serverless\"},\"identity\":{\"type\":\"SystemAssigned\"},\"properties\":{\"authOptions\":{\"aadOrApiKey\":{\"aadAuthFailureMode\":\"http401WithBearerChallenge\"}}}}" \
    -o none
fi

echo "== Retriever 1 needs paid knowledge retrieval (no free tier)"
az rest --method patch --url "$SEARCH_URL" --body '{"properties":{"knowledgeRetrieval":"standard"}}' -o none

echo "== storage account (graph extraction needs blob soft delete ON and versioning OFF)"
az storage account create -n "$STORAGE" -g "$RG" -l "$LOC" --sku Standard_LRS --kind StorageV2 \
  --allow-blob-public-access false --min-tls-version TLS1_2 -o none
az storage account blob-service-properties update -n "$STORAGE" -g "$RG" \
  --enable-delete-retention true --delete-retention-days 7 --enable-versioning false -o none
az storage container create -n "$CONTAINER" --account-name "$STORAGE" --auth-mode login -o none

echo "== Foundry resource and model deployments"
az cognitiveservices account create -n "$FOUNDRY" -g "$RG" -l "$LOC" --kind AIServices --sku S0 \
  --custom-domain "$FOUNDRY" --assign-identity --yes -o none
az cognitiveservices account deployment create -n "$FOUNDRY" -g "$RG" --deployment-name "$CHAT_MODEL" \
  --model-name "$CHAT_MODEL" --model-version "$CHAT_VERSION" --model-format OpenAI \
  --sku-name GlobalStandard --sku-capacity 250 -o none
az cognitiveservices account deployment create -n "$FOUNDRY" -g "$RG" --deployment-name "$EMBED_MODEL" \
  --model-name "$EMBED_MODEL" --model-version "$EMBED_VERSION" --model-format OpenAI \
  --sku-name GlobalStandard --sku-capacity 250 -o none

echo "== role assignments"
SEARCH_ID="/subscriptions/$SUB/resourceGroups/$RG/providers/Microsoft.Search/searchServices/$SEARCH"
STORAGE_ID="$(az storage account show -n "$STORAGE" -g "$RG" --query id -o tsv)"
FOUNDRY_ID="$(az cognitiveservices account show -n "$FOUNDRY" -g "$RG" --query id -o tsv)"
SEARCH_MI="$(az rest --method get --url "https://management.azure.com$SEARCH_ID?api-version=$SEARCH_API" --query identity.principalId -o tsv)"

assign() {
  az role assignment create --assignee-object-id "$1" --assignee-principal-type "$2" --role "$3" --scope "$4" -o none \
    || echo "WARN: could not assign '$3' to $1"
}
# Search service identity reads blobs and calls the models
assign "$SEARCH_MI" ServicePrincipal "Storage Blob Data Reader" "$STORAGE_ID"
assign "$SEARCH_MI" ServicePrincipal "Cognitive Services OpenAI User" "$FOUNDRY_ID"
# Signed-in user manages search objects, uploads blobs and calls models
assign "$ME" User "Search Service Contributor" "$SEARCH_ID"
assign "$ME" User "Search Index Data Contributor" "$SEARCH_ID"
assign "$ME" User "Storage Blob Data Contributor" "$STORAGE_ID"
assign "$ME" User "Cognitive Services OpenAI User" "$FOUNDRY_ID"

echo "== write .env"
cat > "$(dirname "$0")/../.env" <<EOF
AZURE_SUBSCRIPTION_ID=$SUB
RESOURCE_GROUP=$RG
SEARCH_ENDPOINT=https://$SEARCH.search.windows.net
SEARCH_API_VERSION=2026-11-01-preview
STORAGE_ACCOUNT=$STORAGE
STORAGE_RESOURCE_ID=$STORAGE_ID
CONTAINER_NAME=$CONTAINER
MODEL_ENDPOINT=https://$FOUNDRY.openai.azure.com
CHAT_DEPLOYMENT=$CHAT_MODEL
EMBEDDING_DEPLOYMENT=$EMBED_MODEL
EOF
echo "done"
