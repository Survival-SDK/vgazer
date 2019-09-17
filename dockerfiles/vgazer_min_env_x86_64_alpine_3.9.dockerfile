FROM alpine:3.9 as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apk add --no-cache sudo \
    && sed -e 's/# %wheel ALL=(ALL) NOPASSWD: ALL/%wheel ALL=(ALL) NOPASSWD: ALL/g' -i /etc/sudoers \
    && adduser --disabled-password -S vgazer_user \
    && sed -e 's/^wheel:\(.*\)/wheel:\1,vgazer_user/g' -i /etc/group
USER vgazer_user
RUN sudo apk add --no-cache python3 \
    && sudo pip3 install --upgrade pip \
    && sudo pip3 install requests bs4
WORKDIR /vgazer
