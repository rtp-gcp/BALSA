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
    - AppSpot
        - for 'Authorised JavaScript origins': https://YOUR_APPENGINE.com
        - for 'Authorised redirect URIs': https://YOUR_APPENGINE.com/login/callback
    - DNS ie. balsa.rtp-gcp.org
        - for 'Authorised JavaScript origins': https://YOUR_APP.rtp-gcp.org
        - for 'Authorised redirect URIs': https://YOUR_APP.rtp-gcp.org/login/callback


The `.env` file should look like this:

```
# in gcp console from hamburger menu in left sidebar
# = : API APIs & Services -> Credentials -> OAuth 2.0 Client IDs ->
# Client Secrets on Right hand side of page
SECRET_KEY="from client secrets entry"
# Additional Information on Right hand side of page at top
CLIENT_ID="from Client ID entry"
# These need to be added to lower left under the section
# titled "Authorized Redirect URIs"
# Currently, I have both specified.  
# For code, I am only using the DNS version and not
# the appspot one.
# If using appspot
#LOGIN_URI="https://balsa-404914.uc.r.appspot.com/login/callback"
# If using DNS
LOGIN_URI="https://balsa.rtp-gcp.org/login/callback"

# This is the OPEN API key
OPENAI_API_KEY="put key here"


GPT_DEFAULT_MODEL="gpt-3.5-turbo-1106"

# This is the tuned model key
GPT_TUNED_MODEL=""

ADMIN="admin@gmail.com"

```


## Balsa.rtp-gcp.org notes

Need to use the google search page.  See [here](https://search.google.com/search-console?utm_source=about-page&resource_id=sc-domain:rtp-gcp.org)



## firestore db

Create a firestore db in native mode
```
gcloud firestore databases create --type=firestore-native --location=nam5
```
- create collection 'allowed_users' and for each user create a document with email assigned to document ID

## stuff cut

```
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  ```