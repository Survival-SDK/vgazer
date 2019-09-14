FROM debian:stretch as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update && apt-get -y install sudo
RUN useradd -m vgazer_user \
    && echo "vgazer_user:vgazer_user" | chpasswd \
    && adduser vgazer_user sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER vgazer_user
# Fail to install libssl1.0.2 needed by cmake without this step
RUN sudo bash -c 'echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list' \
    && sudo apt-get update
RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip
RUN pip3 install requests
RUN pip3 install bs4
WORKDIR /vgazer
