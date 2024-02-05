FROM debian:buster as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN echo "deb http://ftp.debian.org/debian buster-backports main" \
    > /etc/apt/sources.list.d/backports.list \
    && apt-get update \
    && apt-get install -y python3 python3-venv python3-requests python3-bs4 git
WORKDIR /mnt/vgazer
