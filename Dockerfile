FROM python:3.11-buster

WORKDIR /usr/src/app
COPY . .

RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
