FROM python:3.7-alpine3.9

COPY docker-entrypoint.sh docker-entrypoint.sh


COPY requirements.txt src/
ADD . /src/
WORKDIR /src/

RUN apk update && apk add libpq wkhtmltopdf
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip3 install -r requirements.txt \
    && apk del --no-cache .build-deps

RUN chmod 755 django_runserver.sh

CMD ["sh", "docker-entrypoint.sh "]