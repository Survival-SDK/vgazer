FROM oraclelinux:7-slim as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN yum -y install python3 python3-pip git \
 && pip3 install requests bs4 multimethod yolk3k
WORKDIR /mnt/vgazer
