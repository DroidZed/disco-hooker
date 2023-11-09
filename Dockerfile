# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY src ./src

EXPOSE 6000

ENTRYPOINT ["waitress-serve", "--host", "0.0.0.0", "--port", "6000", "--call", "app:create_app"]
