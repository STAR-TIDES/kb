# FROM node:14.17-stretch as node_builder
# WORKDIR /app
# COPY ./frontend/star-tides ./frontend/star-tides
# WORKDIR /app/frontend/star-tides
# RUN npm i --no-verbose
# RUN npm i -g @angular/cli@latest
# RUN ng build --no-verbose --deploy-url='/static'
# WORKDIR /app


# FROM python:3.7-stretch as python_builder
# WORKDIR /
# COPY ./star_tides/requirements.txt /tmp/requirements.txt
# RUN pip3 install -r /tmp/requirements.txt
# WORKDIR /app
# COPY --from=node_builder /app/frontend/star-tides/dist/star-tides /app/static/
# RUN ls -l static
# CMD python3 run.py

FROM debian:buster-slim
WORKDIR /app
COPY . .
RUN set -x && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3 curl software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN (cd ./frontend/star-tides && nodejs --version && npm i && npm i -g @angular/cli@latest && ng build --no-verbose --deploy-url='/static')
RUN (cp .frontend/star-tides/dist/star-tides /app/static)
RUN (pip3 install -r ./star_tides/requirements.txt)
CMD python3 run.py