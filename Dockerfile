FROM python:3

COPY requirements.txt src/
ADD . /src/
WORKDIR /src/
RUN pip3 install -r requirements.txt

