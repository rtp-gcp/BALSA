#!/bin/bash

# Visit https://cloud.google.com/sdk/docs/install for the latest version
VERSION=google-cloud-cli-454.0.0-linux-x86_64.tar.gz
DOWNLOAD_PATH=/home/codespace/

# Download the installation archive
echo "Downloading Google Cloud SDK"
curl -o ${DOWNLOAD_PATH}${VERSION} https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/${VERSION}

# Extract the archive
tar -xf ${DOWNLOAD_PATH}${VERSION} -C ${DOWNLOAD_PATH}

${DOWNLOAD_PATH}google-cloud-sdk/install.sh

${DOWNLOAD_PATH}google-cloud-sdk/bin/gcloud init
