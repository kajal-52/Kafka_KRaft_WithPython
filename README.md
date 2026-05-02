# Kafka KRaft with Python Client   

## Table of Contents
- [Overview](##Overview)
- [Architecture](##Architecture)
- [Usage](##Usage)
- [Resources](##Resources)

## Overview
This project demonstrates how to use Apache Kafka in KRaft mode with Python clients (producer & consumer).

#### What does it do?
- Runs Kafka in KRaft mode (no ZooKeeper)
- Uses Python to:
   - Produce messages to a Kafka topic.
   - Consume messages from that topic.

#### What is KRaft Mode?
KRaft simplifies Kafka by removing ZooKeeper and managing metadata internally using a Raft-based quorum.

## Architecture 
Demonstrates event-driven architecture

#### Core Components

<img width="586" height="285" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/12452108-c05e-45e8-8d12-3f2f55e3920a" />

## Usage

- Step 1: Clone the repository to your local machine.
- Step 2: Open the project in PyCharm (or any preferred IDE).
- Step 3: Start the Kafka cluster using Docker:
   Run docker-compose up from the terminal (or use the IDE’s Docker integration if available)
- Step 4: Run the producer script to send messages to Kafka.
- Step 5: Run the consumer script to receive messages from the Kafka topic.
- Step 6: Explore Kafka CLI commands to inspect topics and messages and debug the system.

## Resources
[Kafka Crash Course - Hands-On Project](https://www.youtube.com/watch?v=B7CwU_tNYIE)

