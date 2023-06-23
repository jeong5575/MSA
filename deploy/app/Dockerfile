FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libmariadb3 libmariadb-dev
RUN apt-get -y install gcc

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app