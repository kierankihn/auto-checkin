FROM alpine:latest

WORKDIR ./app

ADD . .

RUN apk add --update py3-pip

RUN pip3 install -r requirements.txt --break-system-packages

RUN apk add --no-cache tzdata

CMD ["python3", "-u", "./main.py"]