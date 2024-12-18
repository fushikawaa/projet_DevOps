# Utiliser une image Python comme base
FROM python:3.9-slim

# Copier les fichiers du script
WORKDIR /app
COPY kafka_consumer.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Variables d'environnement pour BigQuery
ENV GOOGLE_APPLICATION_CREDENTIALS=/secret/service-account.json

# Copier les credentials BigQuery
COPY secret/service-account.json /secret/service-account.json

# Commande pour lancer le consumer
CMD ["python3", "kafka_consumer.py"]
