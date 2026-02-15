FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    jq \
    && rm -rf /var/lib/apt/lists/*

RUN echo '#!/bin/bash' > /entrypoint.sh && chmod +x /entrypoint.sh

WORKDIR /app

COPY environment/input.json /app/input.json

ENTRYPOINT ["/entrypoint.sh"]
