FROM python:3.12-slim

# Install GCC build dependency
RUN apt-get update \
    && apt-get install -y gcc g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm 

COPY *.py /app
COPY entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]