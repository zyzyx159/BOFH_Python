FROM python:3.12

WORKDIR /app

# Install system dependencies
COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y xvfb x11-apps libnss3 libxss1 libasound2 fonts-noto-color-emoji cron nano

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Playwright dependencies
RUN playwright install-deps chromium
RUN playwright install chromium

# Copy cron file and set up logging
# COPY crontab /etc/cron.d/my-cron
# RUN chmod 0644 /etc/cron.d/my-cron
# RUN touch /var/log/cron.log

# Copy application code
COPY . /app

# Set environment variable for display (helpful for debugging, but xvfb-run sets it automatically)
ENV DISPLAY=:99

# Use xvfb-run to wrap the command passed to the container
ENTRYPOINT ["/usr/bin/xvfb-run", "-a", "--server-args=-screen 0 1024x768x16"]
CMD ["python", "main.py"]  # Replace with your actual command   