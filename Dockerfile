FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Upewnij się, że katalog /app ma odpowiednie uprawnienia
RUN chown -R nobody:nogroup /app && \
    chmod -R 755 /app && \
    touch /app/honeypot.log && \
    chmod 666 /app/honeypot.log

USER nobody

CMD ["python", "app.py"]