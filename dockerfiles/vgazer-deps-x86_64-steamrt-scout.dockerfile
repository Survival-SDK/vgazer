FROM registry.gitlab.steamos.cloud/steamrt/scout/sdk:latest-steam-client-general-availability as build
MAINTAINER Vasiliy Edomin <Vasiliy.Edomin@gmail.com>
RUN apt-get update \
 && apt-get remove -y libssl-dev \
 && update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-9 1 \
 # && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 1 \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 1 \
 && update-alternatives --set cpp-bin /usr/bin/cpp-9 \
 && update-alternatives --install /usr/bin/gcc-ar gcc-ar /usr/bin/gcc-ar-9 1 \
 && update-alternatives --install /usr/bin/gcc-nm gcc-nm /usr/bin/gcc-nm-9 1 \
 && update-alternatives --install /usr/bin/gcc-ranlib gcc-ranlib \
    /usr/bin/gcc-ranlib-9 1 \
 && update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-9 1
WORKDIR /tmp
RUN curl https://www.openssl.org/source/openssl-1.1.1t.tar.gz \
    -o openssl-1.1.1t.tar.gz \
 && tar -xvf openssl-1.1.1t.tar.gz
WORKDIR /tmp/openssl-1.1.1t
RUN ./Configure --prefix=/usr/local no-zlib linux-x86_64 --openssldir=/etc/ssl \
 && make \
 && make install_sw
WORKDIR /tmp
RUN curl https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tgz \
    -o Python-3.11.2.tgz \
 && tar -xvf Python-3.11.2.tgz
WORKDIR /tmp/Python-3.11.2
RUN ./configure --prefix=/usr/local --disable-test-modules --with-lto=yes \
     --with-doc-strings=no --with-openssl=/usr/local --with-openssl-rpath=auto \
 && make \
 && make altinstall \
 && update-alternatives --install /usr/bin/python3 \
     python3 /usr/local/bin/python3.11 1 \
 && update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.11 1
WORKDIR /tmp
RUN curl https://files.pythonhosted.org/packages/d2/f4/274d1dbe96b41cf4e0efb70cbced278ffd61b5c7bb70338b62af94ccb25b/requests-2.28.2-py3-none-any.whl \
    -o requests-2.28.2-py3-none-any.whl \
 && pip3 install ./requests-2.28.2-py3-none-any.whl \
 && curl https://files.pythonhosted.org/packages/7b/f5/890a0baca17a61c1f92f72b81d3c31523c99bec609e60c292ea55b387ae8/urllib3-1.26.15-py2.py3-none-any.whl \
    -o urllib3-1.26.15-py2.py3-none-any.whl \
 && pip3 install ./urllib3-1.26.15-py2.py3-none-any.whl \
 && curl https://files.pythonhosted.org/packages/ee/a7/06b189a2e280e351adcef25df532af3c59442123187e228b960ab3238687/beautifulsoup4-4.12.0-py3-none-any.whl \
    -o beautifulsoup4-4.12.0-py3-none-any.whl \
 && pip3 install ./beautifulsoup4-4.12.0-py3-none-any.whl \
 && curl https://files.pythonhosted.org/packages/b6/71/42263a6b7555ec36799b39095b93e6097da61e2c184edb8bed5924493682/multimethod-1.11-py3-none-any.whl \
    -o multimethod-1.11-py3-none-any.whl \
 && pip3 install ./multimethod-1.11-py3-none-any.whl
WORKDIR /mnt/vgazer
