# note on gcp


Installing the gcloud sdk.  For some reason, I had problems with the install method on gcp page.  I recommend creating this entry
after attempting to do what is in the doc.  I blame github codespaces using azure and ubuntu.  I normally use debian, so you got me.

The instructions will provide this section, it can be verified using root:

```
$ cd /etc/apt
/etc/apt $ cat sources.list.d/google-cloud-sdk.list 
deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main
```

As root do this (from the google docs on "if doesn't support apt-key"):

```
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.asc
```


Afterwords, you can do:

```
$ sudo apt-get update
$ sudo apt-get install google-cloud-cli
$ gcloud init
```

FWIW, I could do this command but it did not work.  It would pull a public key but just not permit apt-get to work

```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B53DC80D13EDEF05
```

## CLI tips

Use this command to get info about current gcloud CLI account project name and email.

```
$ gcloud config list
```

## project notes

* project names need dashes and not underscores.

# URLS

* [cloud sdk install](https://cloud.google.com/sdk/docs/install)


# switch to native mode in firestore

The oauth2 stuff is in the api and credentials page

```
# not needed
gcloud auth login
# when done the prompt will show the project name
gcloud config set project balsa-404914
gcloud alpha firestore databases update --type=firestore-native
```