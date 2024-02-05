FROM debian:stretch as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN echo "deb http://archive.debian.org/debian/ stretch contrib main non-free" \
    > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y python3 python3-venv python3-requests python3-bs4 git
    # && apt-get install -y python3 python3-pip git\
    # && pip3 install requests bs4
WORKDIR /mnt/vgazer
