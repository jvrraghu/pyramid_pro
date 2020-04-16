#!/bin/bash
FROM ubuntu:16.04
FROM python:3.7

RUN mkdir -p ~/ws/pyramid/ && virtualenv $work_dir && source  $work_dir/bin/activate && pip install --upgrade pip && pip install pyramid==1.10.4

WORKDIR ~/ws/pyramid/

ADD app.py app.py

CMD ["python", "app.py"]
