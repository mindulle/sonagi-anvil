# Chat App System Design Summary

## 1. Core Requirements
- Real-time messaging (low latency).
- Scalable backend (multiple servers).

## 2. Key Architectural Components
- **Protocol:** Use **WebSocket** for persistent, bidirectional communication. HTTP Polling is an anti-pattern.
- **Scalability:** Since users can be connected to different servers, use a **Pub/Sub (e.g., Redis Pub/Sub, Kafka)** system to route messages between servers.
- **Storage:** Use a fast NoSQL database for chat history and a relational database for user/group management if needed.

## 3. Key Takeaway
- Avoid HTTP polling for real-time applications.
- Understand the Pub/Sub model for distributed systems.
