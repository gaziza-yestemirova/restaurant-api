FROM python:3.9.7-alpine3.14
ENV PYTHONUNBUFFERED=1

ADD ./src/requirements.txt /src/

RUN apk update \
    && apk --no-cache add bash postgresql-dev \
    binutils gdal-dev \
# Add build dependencies
    && apk --no-cache add --virtual .build-deps \
    tzdata libffi-dev gcc g++ curl-dev libressl-dev \
    musl-dev cmake make \
# Upgrade pip
    && pip install --upgrade pip wheel setuptools \
# Add project dependencies
    && pip install -Ur /src/requirements.txt

COPY ./src /src

WORKDIR /src

CMD ["./entrypoint.sh"]
