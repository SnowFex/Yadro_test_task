FROM ubuntu:22.04 AS builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

FROM builder

COPY search_path.sh extract_path_value.py config.txt /tmp/