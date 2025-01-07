FROM python:3.12-slim as build

# set working dirctory

WORKDIR /app

# install build dependencies

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]