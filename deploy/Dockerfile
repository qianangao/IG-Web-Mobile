FROM python:3.6.8

ENV http_proxy="http://10.57.197.116:50030" \
    https_proxy="https://10.57.197.116:50030"

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libtiff5-dev \
    liblcms2-dev \
    libfreetype6-dev \
    libwebp-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libopenjp2-7-dev

RUN pip uninstall pillow && \
    CC="cc -mavx2" pip install --no-cache-dir -U -I --force-reinstall pillow-simd==6.0.0.post0 \
        --global-option="build_ext" \
        --global-option="--enable-zlib" \
        --global-option="--enable-jpeg" \
        --global-option="--enable-tiff" \
        --global-option="--enable-freetype" \
        --global-option="--enable-lcms" \
        --global-option="--enable-webp" \
        --global-option="--enable-webpmux" \
        --global-option="--enable-jpeg2000"

WORKDIR /app

ADD . /app

RUN chmod a+x run.sh

RUN pip install -r requirements.txt --no-index --find-links=requirements && \
    cp /usr/share/zoneinfo/Hongkong /etc/localtime && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

# 取消代理设置
ENV http_proxy="" \
    https_proxy=""

EXPOSE 5000

CMD /app/run.sh
