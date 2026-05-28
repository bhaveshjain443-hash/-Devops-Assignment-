# DevOps AI Backend Assignment

## Project Overview

This project demonstrates a production-style backend deployment using FastAPI, Docker, Docker Compose, PostgreSQL, Redis, Celery, and NGINX.

The application supports asynchronous background task execution using Celery workers and Redis as the message broker.

The project also includes CI/CD automation using GitHub Actions.

---

# Tech Stack

* FastAPI
* Docker
* Docker Compose
* PostgreSQL
* Redis
* Celery
* NGINX
* GitHub Actions
* Linux (Ubuntu)

---

# Architecture

```text
User
  ↓
NGINX Reverse Proxy
  ↓
FastAPI Backend
  ↓
Redis Message Broker
  ↓
Celery Worker

FastAPI
  ↓
PostgreSQL Database
```

---

# Folder Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── worker.py
│   ├── tasks.py
│   └── requirements.txt
│
├── nginx/
│   └── nginx.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
└── architecture.png
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/bhaveshjain443-hash/-Devops-Assignment-.git
```

---

## Build and Start Application

```bash
docker compose up -d --build
```

---

## Verify Running Containers

```bash
docker ps
```

Expected containers:

* fastapi_app
* celery_worker
* postgres_db
* redis_cache
* nginx_proxy

---

# API Endpoints

## Home Endpoint

```text
GET /
```

Example:

```text
http://localhost:8090/
```

---

## Health Check Endpoint

```text
GET /health
```

Example:

```text
http://localhost:8090/health
```

---

## Run Async Task

```text
GET /add/10/20
```

Example:

```text
http://localhost:8090/add/10/20
```

Response:

```json
{
  "task_id": "sample-task-id",
  "message": "Task Submitted"
}
```

---

## Get Task Result

```text
GET /result/{task_id}
```

Example:

```text
http://localhost:8090/result/sample-task-id
```

---

# Docker Compose Services

## FastAPI

Main backend API service.

---

## PostgreSQL

Stores application data.

---

## Redis

Used as message broker for Celery workers.

---

## Celery Worker

Executes asynchronous background tasks.

---

## NGINX

Acts as reverse proxy and forwards requests to FastAPI service.

---

# CI/CD Pipeline

GitHub Actions is used to automate Docker build workflow whenever code is pushed to the main branch.

Workflow file:

```text
.github/workflows/deploy.yml
```

Pipeline steps:

1. Checkout repository
2. Build Docker containers
3. Validate deployment workflow

---

# Security Measures

* Docker internal networking
* Environment variable configuration
* Reverse proxy using NGINX
* Container isolation
* SSL-ready deployment architecture
* Services communicate internally through Docker network
* Only NGINX is intended to be publicly exposed

---

# Monitoring Strategy

The following methods are used for monitoring and troubleshooting:

* Docker logs
* Container health monitoring
* Health check endpoint
* NGINX logs
* Application logs

Useful commands:

```bash
docker ps
docker logs fastapi_app
docker logs celery_worker
docker logs nginx_proxy
```

---

# Backup Strategy

* PostgreSQL persistent volume used for database persistence
* Planned cron-based backup support
* Docker restart policies enabled



---

# Troubleshooting

## Check Running Containers

```bash
docker ps
```

---

## Check Container Logs

```bash
docker logs fastapi_app
docker logs celery_worker
docker logs nginx_proxy
```

---

## Restart Services

```bash
docker compose restart
```

---

## Rebuild Containers

```bash
docker compose up -d --build
```

---

# Production Deployment Notes

For local development, a custom host port is used to avoid local machine port conflicts.

In production deployment:

* NGINX can expose port 80
* SSL can be configured using Let's Encrypt
* Deployment can run on AWS EC2 or any Linux VPS
* Reverse proxy architecture improves security and scalability

---

# Infrastructure Design

```text
Internet
   ↓
AWS VPC
   ↓
Public Subnet
   ↓
EC2 Ubuntu Server
   ↓
Docker Compose Stack
   ↓
NGINX → FastAPI → Redis/PostgreSQL
```

---

# Future Improvements

* HTTPS using Let's Encrypt
* Prometheus and Grafana monitoring
* Automated backups
* Zero-downtime deployment
* Kubernetes deployment support

---

# Assignment Summary

This project demonstrates:

* Docker containerization
* Multi-container orchestration
* Reverse proxy setup
* Background task processing
* Redis integration
* CI/CD automation
* Production troubleshooting
* Linux-based deployment workflow
* Production-style architecture
