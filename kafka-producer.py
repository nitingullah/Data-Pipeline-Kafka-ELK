# from faker import Faker
from kafka import KafkaProducer
from data import get_registered_user
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=["192.168.1.4:9092"],
    value_serializer=json_serializer
)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("single-partition-topic", registered_user)
        time.sleep(3)