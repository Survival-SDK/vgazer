FROM debian:stretch as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update && apt-get -y install sudo
RUN useradd -m test_user \
    && echo "test_user:test_user" | chpasswd \
    && adduser test_user sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER test_user
RUN sudo bash -c 'echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list' \
    && sudo apt-get update
RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip
RUN pip3 install requests
RUN pip3 install bs4
WORKDIR /vgazer
