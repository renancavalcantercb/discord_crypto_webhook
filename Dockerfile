FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN echo "Installing dependencies..."
RUN pip install -r requirements.txt

COPY .env .
COPY src/ ./src/
COPY crontab .

RUN echo "Setting up cron task..."
RUN apt-get update && apt-get -y install cron
COPY crontab /etc/cron.d/crypto-cron
RUN chmod 0644 /etc/cron.d/crypto-cron
RUN crontab /etc/cron.d/crypto-cron
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
