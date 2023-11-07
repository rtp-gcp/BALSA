# Creating service accounts for notebooks


## Authentication

### Set and create
```
$ SERVICE_ACCOUNT_ID=jams-devpost
$ gcloud iam service-accounts create $SERVICE_ACCOUNT_ID  \
    --description="A custom service account for Vertex custom training with Tensorboard" \
    --display-name="Vertex AI Custom Training"
```
## Authorization

### cloud storage

```
$ PROJECT_ID=$(gcloud config get-value core/project)
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/storage.admin"
```

### App engine

App Engine default service account	
Editor

```
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/appengine.appAdmin"
```


### Vertex AI

```
$ gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com \
    --role="roles/aiplatform.serviceAgent"
 ```
    

## create the json key

```
$ gcloud iam service-accounts keys create ~/path/to/your-key-file.json --iam-account SERVICE_ACCOUNT_NAME@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

