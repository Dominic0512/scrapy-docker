FROM alpine:edge
MAINTAINER Dominic Lee
RUN apk --update --no-cache add python-pip python-dev ca-certificates musl-dev musl-utils musl-dbg gcc libevent-dev  \
  libxml2-dev libxslt-dev libffi-dev openssl-dev
RUN pip install --no-cache-dir --upgrade pip
RUN cp -r /usr/include/libxml2/libxml/ /usr/include
RUN pip install --no-cache-dir scrapy scrapyd pymongo