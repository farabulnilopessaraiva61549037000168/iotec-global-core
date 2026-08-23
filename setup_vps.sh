#!/bin/bash
echo "=================================================="
echo "   INICIANDO INSTALAÇÃO AUTOMÁTICA DA IOTEC VPS  "
echo "=================================================="

# Atualiza pacotes e instala Docker + Docker Compose
sudo apt update -y
sudo apt install -y docker.io docker-compose-v2 curl git

# Habilita e inicia o serviço Docker
sudo systemctl enable docker
sudo systemctl start docker

# Subindo o container da IOTEC
cd /app/IOTEC
sudo docker compose down --remove-orphans || true
sudo docker compose up -d --build

echo ""
echo "=================================================="
echo "  IOTEC FOI DEPLOYADA E ESTÁ RODANDO 24/7 NA VPS! "
echo "=================================================="
sudo docker ps