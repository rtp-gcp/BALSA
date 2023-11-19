# BalsaFe

##### Balsa Front End 
Python Webapp for the user to get code assistance



# notes on deploy

https://cloud.google.com/appengine/docs/flexible/configure-service-accounts
https://cloud.google.com/appengine/docs/legacy/standard/python/user-managed-service-accounts#gcloud

gcloud app deploy --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
gcloud app deploy --service-account=jams-devpost-sa@jams-devpost.iam.gserviceaccount.com

update the service account name

gcloud app update --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
gcloud app update --service-account=jams-devpost-sa@jams-devpost.iam.gserviceaccount.com


