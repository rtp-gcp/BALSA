

# create service account json file
export YOUR_PROJECT_ID="balsa-404914"
export SERVICE_ACCOUNT_ID="balsa-sa"
gcloud iam service-accounts keys create /workspaces/BALSA/webapps/gcp_key_file.json --iam-account ${SERVICE_ACCOUNT_ID}@${YOUR_PROJECT_ID}.iam.gserviceaccount.com