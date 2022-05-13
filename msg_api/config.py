producer_config = {
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '3TUUWVUFACPOGJNT',
    'sasl.password': 'SWFLvqA6bdr0+xw9/Os9wTF2PUv810w5HsQVF33+4s73KyVYWEat2KS/2pJLCBUr',
}

consumer_config = {
    'bootstrap.servers': 'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '3TUUWVUFACPOGJNT',
    'sasl.password': 'SWFLvqA6bdr0+xw9/Os9wTF2PUv810w5HsQVF33+4s73KyVYWEat2KS/2pJLCBUr',
    'group.id': 'example',
    'auto.offset.reset': 'earliest',
}

