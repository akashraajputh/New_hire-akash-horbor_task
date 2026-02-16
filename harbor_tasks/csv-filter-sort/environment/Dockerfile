FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN echo '#!/bin/bash' > /entrypoint.sh && echo 'exec "$@"' >> /entrypoint.sh && chmod +x /entrypoint.sh

WORKDIR /app

COPY products.csv /app/products.csv

ENTRYPOINT ["/entrypoint.sh"]
