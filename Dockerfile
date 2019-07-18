# We're using Alpine stable
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/v3.9/community;http\1/v3.9/community;g' -i /etc/apk/repositories

# Installing Python
RUN apk add --no-cache --update \
    git \
    dash \
    libffi-dev \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    readline-dev \
    sqlite-dev \
    build-base \
    python3 \
    libxslt-dev \
    libxml2 \
    libxml2-dev \
    py-pip \
    libpq \
    build-base \
    linux-headers \
    jpeg-dev \
    curl \
    neofetch \
    sudo \
    gcc \
    python-dev \
    python3-dev \
    musl \
    sqlite \
    figlet \
    libwebp-dev \
    chromium \
    chromium-chromedriver

RUN pip3 install --upgrade pip setuptools

# Copy Python Requirements to /app

RUN  sed -e 's;^# \(%wheel.*NOPASSWD.*\);\1;g' -i /etc/sudoers
RUN adduser bot --disabled-password --home /home/bot
RUN adduser bot wheel
USER bot
RUN mkdir /home/bot/bot
RUN git clone -b master https://github.com/baalajimaestro/Automated-Evaluation /home/userbot/bot
WORKDIR /home/bot/bot

#
#Copies session and config(if it exists)
#

COPY ./selenium-auto-eval.session /home/bot/bot/

#
# Install requirements
#

RUN sudo pip3 install flask telethon selenium requests
CMD ["python3","bot.py"]
