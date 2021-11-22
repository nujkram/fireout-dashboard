FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

RUN ln -sfn /usr/bin/python3.6 /usr/bin/python3 && ln -sfn /usr/bin/python3 /usr/bin/python && ln -sfn /usr/bin/pip3 /usr/bin/pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install pip --upgrade
RUN python -m pip install wheel
RUN python -m pip install incremental

WORKDIR /app
COPY ./src/requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./src /app/
