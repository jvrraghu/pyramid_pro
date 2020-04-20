#!/bin/bash
FROM ubuntu:16.04
FROM python:3.7

RUN apt-get update

RUN apt-get install -y python-pip 

RUN virtualenv pyramid

RUN /bin/bash -c "source /pyramid/bin/activate" && pip install pyramid==1.10.4

ADD app.py app.py

CMD ["python", "app.py"]
