FROM oraclelinux:7-slim as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
# RUN yum -y install oracle-softwarecollection-release-el7
RUN yum -y install python3 python3-pip git \
 && pip3 install requests bs4 multimethod
WORKDIR /mnt/vgazer
