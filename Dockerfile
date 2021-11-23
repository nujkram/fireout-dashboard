FROM python:3.6-slim

RUN apt-get update && apt-get install -y build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install pip --upgrade
RUN python -m pip install wheel
RUN python -m pip install incremental

WORKDIR /app
COPY ./src/requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./src /app/

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
