FROM archlinux:latest as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN pacman-key --init \
 && pacman --noconfirm --disable-download-timeout -Syu \
 && pacman --noconfirm --disable-download-timeout -S python python-pip \
    python-requests python-beautifulsoup4 git
RUN pip3 install --break-system-packages multimethod
WORKDIR /mnt/vgazer
