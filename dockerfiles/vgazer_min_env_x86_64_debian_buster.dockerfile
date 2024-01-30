FROM debian:buster as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update \
    && apt-get install -y wget \
    && mkdir /tmp/.vgazer-build
WORKDIR /tmp/.vgazer-build
RUN echo "deb http://ftp.debian.org/debian buster-backports main" \
    > /etc/apt/sources.list.d/backports.list \
    && apt-get update \
    && apt-get install -y python3 python3-pip \
    && pip3 install requests bs4
WORKDIR /mnt/vgazer
