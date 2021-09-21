# kb
The STAR-TIDES Knowledge Base project.

## Getting Started
Instructions on setting up the local development environment can be found
[here](https://github.com/STAR-TIDES/kb/wiki/Starting-the-dev-environment)


See Google's style pages for info about how we style our code.
[Google style pages](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

Here's a quick reference to [doc strings formatting](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

## Testing

### Frontend

```bash
# Simplest, with file watching and nice Jasmine UI.
$ cd frontend/star-tides && ng test
# Using just docker:
$ docker build -f=./Dockerfile.test-frontend .
# Using docker-compose:
$ docker-compose up --build test-frontend
```

### Backend

```bash
# Using just docker:
$ docker build -f=./Dockerfile.test-backend .
# Using docker-compose:
$ docker-compose up --build test-backend
```

NOTE: `Dockerfile.dev` and `Dockerfile.prod` are used for local development
and production (prod or staging) releases respectively.

## Releases via Cloud Build

We are integrated with Google Cloud Build to build and release `kb` as a self-contained docker
image that combines the frontend and the backend that serves it.

NOTE: We will eventually set up triggers to do automated builds and releases on PRs, merges, etc.

```bash
# Run the Dockerfile locally for production releases.
$ docker build -f=./Dockerfile.prod .
# Remotely run the GCB config for PRs and untrusted code.
$ gcloud builds submit --config=./build-test.cloudbuild.yaml .
# Remotely run the GCB config for releasing merged code to the staging instance.
$ gcloud builds submit --config=./staging.cloudbuild.yaml .
```
