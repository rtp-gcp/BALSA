# Python Webapps


# using a service account to deploy the webapp

These are notes on using a non standard default service account for app engine.  In this case, the service account
will work for both the Vertex AI in the notebooks and App Engine in the webapp.  The service
account is setup in the notebooks.  This is for changing app engine to use the same service 
account.

* [note 1](https://cloud.google.com/appengine/docs/flexible/configure-service-accounts)
* [note 2](https://cloud.google.com/appengine/docs/legacy/standard/python/user-managed-service-accounts#gcloud)


# deploy with specific service account

```
gcloud app deploy --service-account=balsa-sa@balsa-404914.iam.gserviceaccount.com
```

# update the service account name

After this do you need to redeploy? I think not.

```
gcloud app update --service-account=balsa-sa@balsa-404914.iam.gserviceaccount.com
```



# Reference URLs

* [initial guide](https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service)
