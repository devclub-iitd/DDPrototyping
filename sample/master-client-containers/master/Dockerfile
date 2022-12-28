# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /master
# COPY ./requirements.txt requirements.txt
RUN apk update && \
  apk add dos2unix && \
  rm -f /var/cache/apk/*
COPY . .
RUN dos2unix entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]