FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y xvfb x11-apps libnss3 libxss1 libasound2 fonts-noto-color-emoji cron nano
ENTRYPOINT ["/bin/sh", "-c", "/usr/bin/xvfb-run -a $@", ""]
RUN playwright install-deps chromium
RUN playwright install chromium
COPY crontab /etc/cron.d/my-cron
RUN chmod 0644 /etc/cron.d/my-cron
RUN touch /var/log/cron.log
COPY . /app
CMD ["cron", "-f"]