FROM debian:stretch as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN echo "deb http://ftp.de.debian.org/debian stretch main" \
    >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y python3 python3-pip \
    && pip3 install requests bs4
WORKDIR /mnt/vgazer
