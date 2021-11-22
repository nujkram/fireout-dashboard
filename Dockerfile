FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

ENV PYTHONUNBUFFERED=1

RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN python3.6 -m pip install incremental

WORKDIR /app
COPY ./src/requirements.txt requirements.txt
RUN python3.6 -m pip install --no-cache-dir -r requirements.txt
COPY ./src /app/
