
# IoT MQTT Reader

## Overview

This project creates a Python application that connects to a local Mosquitto MQTT broker, listens for messages on the topic `/events`, and logs these messages. 

## Prerequisites

- Docker and Docker Compose installed
- Mosquitto MQTT broker and clients installed

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mqtt-reader.git
   cd mqtt-reader

2. Start the Service:
    ```
    docker compose up --build
    ```
3. Subscribe the topic (preferrably on a new terminal)
    ```
    mosquitto_sub -h localhost -p 1884 -t /events
    ```

4. Publish a message
    ```
    mosquitto_pub -h localhost -p 1884 -t /events -m "Hello, MQTT"
    ```

## Directory Structure
```
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── mqtt_reader
│   └── mqtt_reader.py
└── mosquitto
    ├── config
    │   └── mosquitto.conf
    ├── data
    └── log
```

