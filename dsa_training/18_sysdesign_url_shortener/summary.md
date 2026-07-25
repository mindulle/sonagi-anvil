# URL Shortener System Design Summary

## 1. Core Requirements
- Support 1,000 requests per second (TPS).
- Low latency for URL redirection.

## 2. Key Architectural Components
- **Algorithm:** Use **Base62 encoding** combined with distributed ID generation (e.g., Snowflake) or a pre-generated key service, instead of simple hashing, to avoid collisions and DB overhead.
- **Database Strategy:** The system is **Read-Heavy** (Read:Write ~ 10:1).
- **Caching:** Mandatory integration of a caching layer like **Redis** to store and serve frequent mappings instantly, minimizing DB access.

## 3. Key Takeaway
- Avoid simplistic hashing (like MD5) that leads to collisions in high-concurrency scenarios.
- Always prioritize read-heavy optimizations (Caching) in URL shortening architectures.
