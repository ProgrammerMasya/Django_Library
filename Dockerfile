FROM python:3

COPY db_migrate.sh db_migrate.sh
COPY django_runserver.sh django_runserver.sh

COPY requirements.txt src/
ADD . /src/
WORKDIR /src/

RUN pip3 install -r requirements.txt

CMD ["sh", "db_migrate.sh"]

CMD ["sh", "django_runserver.sh"]