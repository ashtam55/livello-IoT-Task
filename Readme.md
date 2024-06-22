
# IoT MQTT Reader

## Overview

This project creates a Python application that connects to a local Mosquitto MQTT broker, listens for messages on the topic `/events`, and logs these messages. 

## Prerequisites

- Docker and Docker Compose installed
- Mosquitto CLI MQTT client installed

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
    You can use any mqtt client which is installed on your system, if not then you can install clients like Mosquitto, EMQX etc. They comes in both options CLI and GUI.
    I am using Mosquitto CLI for which you have to run the below command to start listening.
    ```
    mosquitto_sub -h localhost -p 1884 -t /events
    ```

4. Publish a message
    ```
    mosquitto_pub -h localhost -p 1884 -t /events -m ‘{“sensor_value”:20.2}’
    ```


## Logs

You can see the logs from the following location - 

```
Mosquitto     - mosquitto/log/mosquitto.log
MQTT/Python   - logs/mqtt_reader.log
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
    │   └── mosquitto.conf
├── logs
│   └── mqtt_reader.log
```

