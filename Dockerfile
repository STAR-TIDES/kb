FROM python:3.7-stretch

COPY ./star_tides/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
WORKDIR /app
CMD python3 run.py