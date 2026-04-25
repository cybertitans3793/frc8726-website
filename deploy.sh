#!/bin/bash
cd /home/ubuntu/frc8726-website
git pull origin main
echo "Deployed at $(date)" >> /home/ubuntu/frc8726-website/deploy.log
