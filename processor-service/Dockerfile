FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y build-essential libpoppler-cpp-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
