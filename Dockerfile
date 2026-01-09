# syntax=docker/dockerfile:1.6
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Create user first
RUN adduser --disabled-password appuser

# Create directories and set proper permissions BEFORE switching to appuser
RUN mkdir -p /app/staticfiles /app/media && \
    chown -R appuser:appuser /app

# Now switch to non-root user
USER appuser

EXPOSE 8000

# Run migrations, collect static files, then start gunicorn
CMD python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput && \
    gunicorn Brain_Page.wsgi:application --bind 0.0.0.0:8000 --workers 3