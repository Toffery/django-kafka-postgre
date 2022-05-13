import requests
import jwt
from confluent_kafka import Consumer
from config import consumer_config


consumer = Consumer(consumer_config)
topic = 'my_topic'
consumer.subscribe([topic])
payload = {
    "role": "post_message_confirm"
}
jwt_token = jwt.encode(payload=payload, key='django-insecure-f)z7g0pr8k)%+vc0-3#%7hmcoe#7ec!@xg2w*pdu*&x2dt+wg-')
headers = {
    "Authorization": jwt_token
}

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            print('Waiting...')
        elif msg.error():
            print(f'ERROR: {msg.error()}')
        else:
            print('Consumed event from topic {topic}: '
                  'key = {key}, value = {value}'.format(topic=msg.topic(),
                                                        key=msg.key().decode('utf-8'),
                                                        value=msg.value().decode('utf-8')))
            if 'абракадабра' not in msg.value().decode('utf-8').lower():
                print('key = {key}, value = {value}, '
                      'status: CORRECT'.format(key=msg.key().decode('utf-8'),
                                               value=msg.value().decode('utf-8')))
                data = {'message_id': msg.key().decode('utf-8'), 'success': True}
            else:
                print('key = {key}, value = {value}, '
                      'status: BLOCKED'.format(key=msg.key().decode('utf-8'),
                                               value=msg.value().decode('utf-8')))
                data = {'message_id': msg.key().decode('utf-8'), 'success': False}

            requests.post('http://127.0.0.1:8000/api/v1/message_confirmation/', json=data, headers=headers)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
