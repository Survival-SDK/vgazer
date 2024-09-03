FROM amazonlinux:2 as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN yum -y install python3 python3-pip python3-requests git \
 && pip3 install bs4 multimethod yolk3k
WORKDIR /mnt/vgazer
