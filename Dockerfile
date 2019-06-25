FROM python:3.7-alpine3.9

COPY Pipfile /
COPY Pipfile.lock /

RUN apk update && apk add libpq libjpeg openjpeg tiff-dev

RUN apk update && apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    # Pillow dependencies
   	libxml2-dev libxslt-dev libffi-dev libgcc openssl-dev curl \
   	jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    libjpeg openjpeg tiff-dev \
    && pip3 install --no-cache-dir pipenv \
    && pipenv install --deploy --system --ignore-pipfile \
    && apk del --no-cache .build-deps

ADD . /src/                                                                                                   
WORKDIR /src/

CMD ["sh", "docker-entrypoint.sh"]
