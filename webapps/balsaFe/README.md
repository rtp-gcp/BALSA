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




## OAuth

Using GCP console create consent screen for auth link [https://console.cloud.google.com/apis/credentials/consent](https://console.cloud.google.com/apis/credentials/consent) 

In API's & Services also create OAuth client ID credentials for web application
- Set URI's:
    - for 'Authorised JavaScript origins': https://YOUR_APPENGINE.com
    - for 'Authorised redirect URIs': https://YOUR_APPENGINE.com/login/callback

In the app.yaml file set env vars:
- CLIENT_ID to given at previous steps value
- LOGIN_URI to https://YOUR_APPENGINE.com/login/callback
- SECRET_KEY to your desired value




## firestore db

Create a firestore db in native mode
```
gcloud firestore databases create --type=firestore-native --location=nam5
```
- create collection 'allowed_users' and for each user create a document with email assigned to document ID

# .env file

The .env file looks like this:

```
SECRET_KEY="somekey from api gcp page"
CLIENT_ID="some email from api gcp page"
LOGIN_URI="https://balsa-404914.uc.r.appspot.com/login/callback"

OPENAI_API_KEY=""

GPT_DEFAULT_MODEL="gpt-3.5-turbo-1106"
GPT_TUNED_MODEL=""

ADMIN="admin@gmail.com"
```