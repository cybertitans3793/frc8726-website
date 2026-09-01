#!/bin/bash
cd /home/pi/frc/frc8726-website
git fetch origin main
git reset --hard origin/main
cd /opt/stacks/frc-website
docker compose down && docker compose up -d
echo "Deployed at $(date)" >> /home/pi/frc/frc8726-website/deploy.log
