from confluent_kafka import Producer
from .config import producer_config


def delivery_callback(err, msg):
    if err:
        print(f'ERROR: Message failed delivery: {err}')
    else:
        print('Produced event to topic {topic}: '
              'key = {key} value = {value}'.format(topic=msg.topic(),
                                                   value=msg.value().decode('utf-8'),
                                                   key=msg.key().decode('utf-8')))


def send(message_id, message):
    topic = 'my_topic'
    producer = Producer(producer_config)
    producer.produce(topic, key=str(message_id), value=message, callback=delivery_callback)
    producer.poll(10000)
    producer.flush()
