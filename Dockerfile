FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN mkdir /app/mp3_queue

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]