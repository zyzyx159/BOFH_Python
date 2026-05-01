#!/bin/bash

# remove lock if server was left running
rm -f /tmp/.X99-lock

# Start Xvfb in the background
Xvfb :99 -screen 0 1280x1024x24 &
export DISPLAY=:99

# Give Xvfb a second to start
sleep 1

# Run your scraper
exec python main.py

