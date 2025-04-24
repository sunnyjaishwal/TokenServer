# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
COPY ./supervisord.conf /etc/supervisord.conf

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update && apt-get install -y supervisor

EXPOSE 8000

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
