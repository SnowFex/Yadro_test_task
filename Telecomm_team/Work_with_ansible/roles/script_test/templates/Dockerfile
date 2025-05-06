FROM ubuntu:22.04 AS builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip && \
    pip install --no-cache-dir requests && \
    rm -rf /var/lib/apt/lists/*

FROM builder

WORKDIR /usr/local/app

COPY script.py /usr/local/app/

RUN useradd -m myuser

USER myuser

CMD ["python3", "/usr/local/app/script.py"]