# pull the official docker image
FROM python:3.9.4-slim
USER root
# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install \
    redis-server
# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt



# copy project
COPY . .