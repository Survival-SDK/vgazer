FROM jimbly/steamrt-amd64:latest as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN useradd -m vgazer_user \
    && echo "vgazer_user:vgazer_user" | chpasswd \
    && adduser vgazer_user sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER vgazer_user
WORKDIR /tmp
RUN sudo apt-get update \
    && sudo update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-5 \
     1 \
    && sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 1 \
    && sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 1 \
    && sudo update-alternatives --install /usr/bin/gcc-ar gcc-ar \
     /usr/bin/gcc-ar-5 1 \
    && sudo update-alternatives --install /usr/bin/gcc-nm gcc-nm \
     /usr/bin/gcc-nm-5 1 \
    && sudo update-alternatives --install /usr/bin/gcc-ranlib gcc-ranlib \
     /usr/bin/gcc-ranlib-5 1 \
    && sudo update-alternatives --install /usr/bin/gcov gcov \
     /usr/bin/gcov-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-cpp \
     x86_64-linux-gnu-cpp /usr/bin/x86_64-linux-gnu-cpp-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-g++ \
     x86_64-linux-gnu-g++ /usr/bin/x86_64-linux-gnu-g++-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-gcc \
     x86_64-linux-gnu-gcc /usr/bin/x86_64-linux-gnu-gcc-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-gcc-ar \
     x86_64-linux-gnu-gcc-ar /usr/bin/x86_64-linux-gnu-gcc-ar-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-gcc-nm \
     x86_64-linux-gnu-gcc-nm /usr/bin/x86_64-linux-gnu-gcc-nm-5 1 \
    && sudo update-alternatives --install \
     /usr/bin/x86_64-linux-gnu-gcc-ranlib x86_64-linux-gnu-gcc-ranlib \
     /usr/bin/x86_64-linux-gnu-gcc-ranlib-5 1 \
    && sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-gcov \
     x86_64-linux-gnu-gcov /usr/bin/x86_64-linux-gnu-gcov-5 1 \
    && sudo update-alternatives --install /usr/bin/pydoc3 pydoc3 \
     /usr/bin/pydoc3.5 1 \
    && sudo update-alternatives --install /usr/bin/pygettext3 pygettext3 \
     /usr/bin/pygettext3.5 1 \
    && sudo update-alternatives --install /usr/bin/python3 python3 \
     /usr/bin/python3.5 1 \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && sudo python3 get-pip.py \
    && pip3 install requests bs4
WORKDIR /mnt/vgazer
