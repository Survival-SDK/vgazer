FROM debian:buster as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update \
    && apt-get install -y sudo \
    && useradd -m vgazer_user \
    && echo "vgazer_user:vgazer_user" | chpasswd \
    && adduser vgazer_user sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER vgazer_user
RUN sudo bash -c 'echo "deb http://deb.debian.org/debian buster-backports main" >> /etc/apt/sources.list' \
    && sudo apt-get update \
    && sudo apt-get install -y python3 python3-pip \
    && pip3 install requests bs4
WORKDIR /vgazer
