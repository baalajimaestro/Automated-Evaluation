# We're using Alpine Edge
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories

# Installing Core Components
RUN apk add --no-cache --update \
    git \
    bash \
    python3 \
    py-pillow \
    py-requests \
    libpq \
    curl \
    sudo \
    neofetch \
    musl \
    py-tz \
    py3-aiohttp \
    py-six \
    py-click \
    xvfb \
    firefox \
    geckodriver

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Clone master by default
#
RUN git clone -b master https://github.com/baalajimaestro/Automated-Evaluation.git /root/userbot

WORKDIR /root/bot/

#
# Copies session and config(if it exists)
#
COPY ./selenium-eval.session /root/bot/

#
# Install dependencies
#
RUN pip3 install selenium xvfbwapper flask requests aiohttp telethon ujson

#
# Finalization
#
CMD ["bash","start.sh"]
