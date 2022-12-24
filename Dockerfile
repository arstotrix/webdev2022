FROM python:3.10

RUN mkdir -p /deploy/app
WORKDIR /deploy/app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - main:app
