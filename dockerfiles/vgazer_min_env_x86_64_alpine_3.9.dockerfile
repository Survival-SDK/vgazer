FROM alpine:3.9 as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apk add --no-cache python3 \
    && pip3 install --upgrade pip \
    && pip3 install requests bs4
WORKDIR /mnt/vgazer
