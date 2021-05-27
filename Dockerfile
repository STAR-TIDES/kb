FROM node:14.17-stretch
COPY \
    ./frontend/star-tides/package.json \
    ./frontend/star-tides/package-lock.json \
    ./frontend/star-tides/angular.json \
    ./frontend/star-tides/tsconfig.json \
    ./frontend/star-tides/tsconfig.app.json\
    ./frontend/star-tides/.browserslistrc \
    /tmp-frontend/
WORKDIR /tmp-frontend/
RUN npm install
COPY ./frontend/star-tides/src /tmp-frontend/src
RUN npm install -g @angular/cli@latest
RUN ng build --no-verbose --deploy-url='/static/'
WORKDIR /tmp-frontend/dist/star-tides
# TODO(ljr): Where does Flask expect the compiled Angular files to be?
COPY . /app/static
COPY . /app/templates

FROM python:3.7-stretch
WORKDIR /
COPY ./star_tides/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
WORKDIR /app
CMD python3 run.py