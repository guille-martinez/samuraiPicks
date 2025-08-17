FROM python:3.11-slim

# Avoid interactive prompts during apt operations
ENV DEBIAN_FRONTEND=noninteractive

# Install system deps only if you hit build issues; keeping it lean first
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Gunicorn will serve Flask app for Cloud Run
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 app:app
