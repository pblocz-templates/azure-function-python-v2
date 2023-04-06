# Find the Dockerfile at this URL
# https://github.com/Azure/azure-functions-docker/blob/dev/host/4/bullseye/amd64/python/python39/python39-core-tools.Dockerfile
FROM mcr.microsoft.com/azure-functions/python:4-python3.9-core-tools


RUN apt-get update && apt-get install -y python3-pip

RUN apt-get remove -y azure-functions-core-tools-4 &&  apt-get update && apt-get install -y "azure-functions-core-tools"
