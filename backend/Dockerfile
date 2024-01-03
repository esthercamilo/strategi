FROM ubuntu:20.04

USER root

ENV DEBIAN_FRONTEND noninteractive
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
ENV APP_HOME=/home/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# Install programs
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3.8 python3-pip
RUN apt install software-properties-common -y
RUN apt install build-essential zlib1g-dev -y libncurses5-dev -y libgdbm-dev libnss3-dev \
 libssl-dev -y libreadline-dev -y libffi-dev -y wget -y
RUN apt-get install -y python-pytest

# Install dependecies
RUN apt-get update -y && \
 apt-get install -y build-essential wget libbz2-dev liblzma-dev libcurl4-openssl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

# copy project
COPY . $APP_HOME
RUN chmod +x /home/app/entrypoint.sh

# run entrypoint
WORKDIR /home/app
ENTRYPOINT ["/home/app/entrypoint.sh"]