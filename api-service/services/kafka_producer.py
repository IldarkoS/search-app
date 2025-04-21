import json
from aiokafka import AIOKafkaProducer
from config import settings

producer = None

async def init_kafka_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    await producer.start()

async def send_upload_event(event: dict):
    await producer.send_and_wait("document_uploaded", event)

async def close_kafka_producer():
    global producer
    if producer:
        await producer.stop()
