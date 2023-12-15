FROM alpine:latest

WORKDIR ./app

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
