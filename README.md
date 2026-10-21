# Multi-Container DevOps Stack

Production-ready local stack featuring Nginx (Reverse Proxy), Python Web Application, and Redis (Cache), containerized with Docker Compose.

## Architecture
- **Nginx**: Reverse proxy listening on port `80`.
- **Web App**: Python container running internally on port `8080`.
- **Cache**: Redis 7 Alpine container on port `6379`.

## Quick Start
1. Clone the repository.
2. Run the stack:
   ```bash
   docker compose up -d --build
