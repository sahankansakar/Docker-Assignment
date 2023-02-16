FROM alpine:3.12

RUN apk add --no-cache \
    python3

COPY . /app
WORKDIR /app


CMD ["python3", "main.py"]
