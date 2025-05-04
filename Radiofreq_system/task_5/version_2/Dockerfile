FROM alpine:3.21.3 AS builder

RUN apk update && \
    apk add --no-cache \
    python3 \
    py3-pip \
    bash \
    && rm -rf /var/cache/apk/*

FROM builder

COPY ../search_path.sh extract_path_value.py config.txt /tmp/