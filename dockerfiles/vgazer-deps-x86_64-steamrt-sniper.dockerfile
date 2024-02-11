FROM registry.gitlab.steamos.cloud/steamrt/sniper/sdk:latest-steam-client-general-availability as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update \
 && apt-get install -y python3 python3-venv python3-pip python3-requests \
    python3-bs4 git \
 && pip3 install multimethod
WORKDIR /mnt/vgazer
