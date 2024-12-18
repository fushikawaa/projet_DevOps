from confluent_kafka import Consumer
from google.cloud import bigquery
import json

# Configurer le client BigQuery
client = bigquery.Client()

# Configurer Kafka Consumer
kafka_config = {
    'bootstrap.servers': 'kafka-broker-service:9092',  # Adresse du broker Kafka
    'group.id': 'bigquery-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(kafka_config)
topic = "posts" 
consumer.subscribe([topic])

def write_to_bigquery(data):
    table_id = "tddevops.my_dataset.my_table"  
    errors = client.insert_rows_json(table_id, [data])
    if errors:
        print(f"Erreur lors de l'insertion : {errors}")
    else:
        print("Données insérées avec succès.")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Erreur Kafka : {msg.error()}")
            continue
        
        message = json.loads(msg.value().decode('utf-8'))  # Décoder le message
        print(f"Message reçu : {message}")
        write_to_bigquery(message)  # Envoyer à BigQuery

except KeyboardInterrupt:
    print("Arrêt du consumer.")
finally:
    consumer.close()
