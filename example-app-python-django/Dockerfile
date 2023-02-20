# FROM python:3.8

# COPY cockroach_example ./cockroach_example
# COPY requirements.txt ./

# RUN pip install -r requirements.txt

# EXPOSE 8080

# CMD ["python", "./cockroach_example/manage.py", "runserver", "0.0.0.0:8080"]

# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /master
# COPY ./requirements.txt requirements.txt
RUN apt-get update && \
  apt-get install dos2unix && \
  rm -f /var/cache/apk/*
COPY cockroach_example ./cockroach_example
COPY requirements.txt ./
COPY entrypoint.sh ./entrypoint.sh
RUN dos2unix entrypoint.sh
RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]