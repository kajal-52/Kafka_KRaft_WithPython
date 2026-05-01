import json

from confluent_kafka import Consumer

consumer_config ={'bootstrap.servers': 'localhost:8092', 'group.id': 'order_tracker', 'auto.offset.reset': 'earliest'}
consumer = Consumer(consumer_config)


consumer.subscribe(['nykaa_orders'])

print(f" consumer is subscribed to nykaa_orders topic ✅")

while True:
    msg = consumer.poll()
    if msg is None:
        continue
    if msg.error():
        print(f" ❌ consumer error: {msg.error()}")
        continue

    value = msg.value().decode('utf-8')
    json_value = json.loads(value)

    print(json_value)

