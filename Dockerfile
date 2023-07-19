FROM python:3.9-slim
LABEL maintainer='azazana'

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./welcomeHome /welcomeHome
WORKDIR /welcomeHome
EXPOSE 8000

ARG DEV="false"
RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
/py/bin/pip install -r /tmp/requirements.txt && \
if [ $DEV = "true" ]; \
then /py/bin/pip install -r /tmp/requirements.dev.txt; \
fi && \
rm -rf /tmp && \
adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER django-user

