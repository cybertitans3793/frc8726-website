#!/bin/bash
cd /home/ubuntu/frc8726-website
git pull origin main
cd /home/ubuntu/frc-website
docker compose down && docker compose up -d
echo "Deployed at $(date)" >> /home/ubuntu/frc8726-website/deploy.log
