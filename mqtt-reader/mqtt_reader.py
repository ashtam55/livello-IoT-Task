import asyncio
from gmqtt import Client as MQTTClient
import logging
import os

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('/app/logs/mqtt_reader.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Ensure no duplicate handlers are added
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Callback when a message is received


def on_message(client, topic, payload, qos, properties):
    logger.info(f"Received message on topic {topic}: {payload.decode()}")


async def main():
    client = MQTTClient("mqtt_reader")

    client.on_message = on_message

    await client.connect("mqtt_broker", port=1884)  # Adjust port if necessary

    client.subscribe("/events")

    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
