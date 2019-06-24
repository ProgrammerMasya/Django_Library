FROM python:3.7-alpine3.9

ADD . /src/
WORKDIR /src/

RUN apk update && apk add libpq
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip3 install --no-cache-dir pipenv \
    && pipenv install --deploy --system \
    && apk del --no-cache .build-deps

CMD ["sh", "docker-entrypoint.sh"]

