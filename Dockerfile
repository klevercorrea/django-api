FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

RUN mkdir /django-api
WORKDIR /django-api

ADD . /django-api/

RUN pip install -r requirements.txt

WORKDIR /django-api/src