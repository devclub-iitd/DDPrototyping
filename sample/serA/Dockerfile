# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /serA
ENV MYSQL_HOST=mysql
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=pwd
ENV MYSQL_DB=databaseA
# COPY ./requirements.txt requirements.txt
RUN apk update && \
  apk add mysql mysql-client && \
  rm -f /var/cache/apk/*
RUN pip install mysql.connector
COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]