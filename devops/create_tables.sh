# Exit immediately if any command fails
set -euo pipefail


# Configuration
PROJECT_ID="association-508416"
LOCATION="asia-southeast1"
DATASET_ID="analytics_db"
SCHEMA_DIR="./schemas"


# ==========================================
# 1. Project Setup & API Activation
# ==========================================
echo "Setting active project: ${PROJECT_ID}"
gcloud config set project "${PROJECT_ID}"

echo "Enabling BigQuery API..."
gcloud services enable bigquery.googleapis.com

# ==========================================
# 2. Create BigQuery Dataset
# ==========================================
if bq show "${PROJECT_ID}:${DATASET_ID}" >/dev/null 2>&1; then
  echo "[!] Dataset '${DATASET_ID}' already exists. Skipping creation."
else
  echo "Creating dataset '${DATASET_ID}' in location '${LOCATION}'..."
  bq mk \
    --location="${LOCATION}" \
    --dataset \
    --description "Automated dataset initialized via setup script" \
    "${PROJECT_ID}:${DATASET_ID}"
fi


# ==========================================
# 3. Loop through all JSON files in the schemas directory
# ==========================================
for schema_path in "${SCHEMA_DIR}"/*.json; do
  # Extract filename without path or extension (e.g., "users.json" -> "users")
  table_name=$(basename "${schema_path}" .json)

  if bq show "${PROJECT_ID}:${DATASET_ID}.${table_name}" >/dev/null 2>&1; then
    echo "[!] Table '${table_name}' already exists. Skipping."
  else
    echo "Creating table '${table_name}' using ${schema_path}..."
    bq mk \
      --table \
      "${PROJECT_ID}:${DATASET_ID}.${table_name}" \
      "${schema_path}"
  fi
done


echo "[SUCCESS] BigQuery setup completed successfully!"
