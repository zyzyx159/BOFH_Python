FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y xvfb
RUN apt-get install -qqy x11-apps
# Additional dependencies for Chromium
RUN apt-get install -y libnss3 libxss1 libasound2 fonts-noto-color-emoji
ENTRYPOINT ["/bin/sh", "-c", "/usr/bin/xvfb-run -a $@", ""]
RUN playwright install-deps chromium
RUN playwright install chromium
COPY . .
CMD ["python", "./main.py"]