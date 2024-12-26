FROM fedora:41 AS build
LABEL org.opencontainers.image.authors="Vasiliy Edomin <Vasiliy.Edomin@gmail.com>"
RUN dnf -y install python3 python3-pip python3-requests python3-beautifulsoup4 \
    git \
 && pip3 install multimethod yolk3k
WORKDIR /mnt/vgazer
