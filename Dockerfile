FROM python:3.6-slim

RUN apt-get update && apt-get install -y build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /home/app
RUN useradd --user-group --shell /bin/bash app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY ./src $APP_HOME
RUN chmod +x $APP_HOME/entrypoint.sh

RUN python -m pip install pip --upgrade
RUN python -m pip install wheel
RUN python -m pip install incremental
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN chown -R app:app /app
RUN chmod +x /app/entrypoint.sh

USER app

ENTRYPOINT ["/app/entrypoint.sh"]
