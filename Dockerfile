FROM python:3.5

RUN pip install pika

RUN mkdir -p /python

WORKDIR /python
