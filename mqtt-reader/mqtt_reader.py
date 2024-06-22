import asyncio
from gmqtt import Client as MQTTClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Callback when a message is received


def on_message(client, topic, payload, qos, properties):
    logger.info(f"Received message on topic {topic}: {payload.decode()}")
    print(payload.decode())
    print("workd")


async def main():
    client = MQTTClient("mqtt_reader")

    client.on_message = on_message

    await client.connect("mqtt_broker", port=1884)

    client.subscribe("/events")
    print("hello")

    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
