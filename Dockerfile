FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app/ ./

CMD ["python","-u","main.py"]