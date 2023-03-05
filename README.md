# Documents Comparision AI Service
An AI service to determine match % for the provided documents

## Why?
To help the opensource world to compare and contract provided documents

## What?
What does this application bring to the table

1. Machine Learning Model to compare the two documents
2. Do the local development without any tools inside the local machine
3. Help debug a Python app inside a Docker container


# How?
A Flask application running in a Dockerized container to compare documents using `scikit-learn` framework

# Setup

## Pre-requisets
1. Install Docker & Docker-compose

## How to run
Run below commands to run the application

```
$ docker-compose build python
$ docker-compose up python
```

Access the application using http://localhost:5003/match

