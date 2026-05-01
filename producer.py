import json
import uuid

from confluent_kafka import Producer


config = {'bootstrap.servers': 'localhost:8092'}
producer = Producer(config)
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: '.format(err))
    else:
        print(f" Message delivered successfully to {msg.value().decode('utf-8')}")
        print(f" delivered to topic {msg.topic()}, partition {msg.partition()},offset {msg.offset()} ")

order =    {"order_id": str(uuid.uuid4()),"user": "Jane Doe", "item" :" The Derma Co Serum","quantity": 1}

val = json.dumps(order).encode("utf-8")

producer.produce("nykaa_orders", value=val, callback=delivery_report)

producer.flush()