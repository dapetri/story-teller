FROM mcr.microsoft.com/devcontainers/python:0-3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /tmp/pip-tmp/
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
