FROM alpine:latest

WORKDIR ./app

ADD . .

RUN apk add --update py3-pip

RUN pip3 install -r requirements.txt --break-system-packages

CMD ["python3", "./main.py"]