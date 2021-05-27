# FROM node:14.17-stretch
# # WORKDIR /app/frontend
# # COPY ./frontend/star-tides/ /
# # RUN npm install
# # RUN npm install -g @angular/cli@latest
# # RUN ng build --no-verbose --deploy-url='/static/'
# # WORKDIR /
# # COPY /app/frontend/dist/star-tides /app/static
# WORKDIR /app/frontend
# COPY ./frontend/star-tides /
# RUN npm install
# RUN npm install -g @angular/cli@latest

FROM node:14.17-stretch
WORKDIR /app
COPY ./frontend/star-tides ./frontend/star-tides
RUN ls -l
# RUN cd ./frontend/star-tides
WORKDIR /app/frontend/star-tides
RUN npm i
RUN npm i -g @angular/cli@latest
RUN ng build --no-verbose --deploy-url='/static/'
RUN ls -l && ls -l dist && ls -l dist/star-tides
WORKDIR /
# RUN ls -l /app/frontend/star-tides/dist/star-tides/
# COPY /app/frontend/star-tides/dist/star-tides/ /app/static/
RUN cp -r /app/frontend/star-tides/dist/star-tides /app/static
RUN mkdir -p /app/star_tides/ && cp -r /app/frontend/star-tides/dist/star-tides /app/star_tides/static
RUN ls -l /app/static 

# FROM python:3.7-stretch
# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# WORKDIR /
# CMD python3 run.py


# FROM node:14.17-stretch
# COPY \
#     ./frontend/star-tides/package.json \
#     ./frontend/star-tides/package-lock.json \
#     ./frontend/star-tides/angular.json \
#     ./frontend/star-tides/tsconfig.json \
#     ./frontend/star-tides/tsconfig.app.json\
#     ./frontend/star-tides/.browserslistrc \
#     /app/frontend/
# WORKDIR /app/frontend
# RUN npm install
# COPY ./frontend/star-tides/src /app/frontend/src/
# RUN npm install -g @angular/cli@latest
# RUN ng build --no-verbose --deploy-url='/static/'
# # WORKDIR /dist/star-tides
# # TODO(ljr): Where does Flask expect the compiled Angular files to be?
# # COPY . /
# # COPY . /app/star_tides/static
# # COPY . /app/star_tides/
# # COPY . /app/static
# # COPY . /app/templates
# # COPY . /static/

# # RUN ls -l /
# # RUN ls -l /app/frontend/dist
# # COPY /app/frontend/dist /app/static
# WORKDIR /
# RUN cp -r /app/frontend/dist/star-tides/ /app/static

# # FROM ubuntu:latest
# # RUN ls -lR

FROM python:3.7-stretch
WORKDIR /
COPY ./star_tides/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
# RUN mkdir /app/static
# RUN echo 'hello' > /app/static/index.html
WORKDIR /app
RUN ls -lR
CMD python3 run.py