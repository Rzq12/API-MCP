FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY api_server.py ./api_server.py

RUN pip install --no-cache-dir .

EXPOSE 8003

CMD ["python", "api_server.py"]