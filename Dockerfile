FROM python:3

COPY django_runserver.sh django_runserver.sh

COPY requirements.txt src/
ADD . /src/
WORKDIR /src/

RUN pip3 install -r requirements.txt

CMD ["sh", "django_runserver.sh"]