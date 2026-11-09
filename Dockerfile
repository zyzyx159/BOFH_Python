# 1. Use the version required by your previous error
FROM mcr.microsoft.com/playwright/python:v1.51.0-noble

# 2. Install Xvfb (Virtual Framebuffer)
RUN apt-get update && apt-get install -y \
    xvfb \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# 3. Set work directory
WORKDIR /app

# 4. Copy requirements and install
# Ensure playwright==1.51.0 is in your requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project (main.py, getLinks.py, .dockerignore, etc.)
COPY . .

RUN mkdir -p /app/output

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
