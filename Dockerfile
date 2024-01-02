FROM alpine:latest as builder

WORKDIR ./app

ADD . .

RUN apk add --update --no-cache tzdata

RUN apk add --update --no-cache py3-pip

RUN apk add --update --no-cache binutils

RUN pip3 install -r requirements-dev.txt --break-system-packages

RUN pyinstaller -F ./main.py

FROM alpine:latest as runner

WORKDIR ./app

COPY --from=builder /app/dist/main /app

CMD ["./main"]