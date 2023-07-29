FROM debian:buster as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update \
    && apt-get install -y wget \
    && echo \
        "deb http://apt.llvm.org/buster/ llvm-toolchain-buster-17 main" \
    > /etc/apt/sources.list.d/llvm.list \
    && mkdir /tmp/.vgazer-build
WORKDIR /tmp/.vgazer-build
RUN wget -qO- https://apt.llvm.org/llvm-snapshot.gpg.key \
    | tee /etc/apt/trusted.gpg.d/apt.llvm.org.asc \
    && echo "deb http://ftp.debian.org/debian buster-backports main" \
    > /etc/apt/sources.list.d/backports.list \
    && apt-get update \
    && apt-get install -y python3 python3-pip \
    && pip3 install requests bs4
WORKDIR /mnt/vgazer
