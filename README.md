# FastAPI Monitoring Demo

This project demonstrates how to monitor a FastAPI application using Prometheus, Grafana, Loki, and Tempo, all orchestrated with Docker Compose. It includes log aggregation, distributed tracing, and load testing.

## Features
- **FastAPI Application**: A simple FastAPI app as the monitored service.
- **Prometheus**: Collects metrics from the FastAPI app.
- **Grafana**: Visualizes metrics, logs, and traces.
- **Loki**: Aggregates and queries logs.
- **Tempo**: Collects distributed traces.
- **Promtail**: Ships logs to Loki.
- **Docker Compose**: Orchestrates all services.
- **Load Testing**: `load_test.py` script for generating traffic.

## Project Structure
```
Fastapi-monitoring-demo/
│
├── docker-compose.yml           # Main Docker Compose file
├── main.py                      # FastAPI application
├── load_test.py                 # Load testing script
├── prometheus.yml               # Prometheus configuration
├── promtail-config.yml          # Promtail configuration
├── tempo-config.yaml            # Tempo configuration
├── logs/
│   └── app.log                  # Application logs
└── ...
```

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.10+

### 1. Clone the Repository
```sh
git clone <repo-url>
cd Fastapi-monitoring-demo
```

### 2. Start All Services
```sh
docker-compose up --build
```
This will start FastAPI, Prometheus, Grafana, Loki, Tempo, and Promtail.

### 3. Access the Services
- **FastAPI**: [http://localhost:8000](http://localhost:8000)
- **Grafana**: [http://localhost:3000](http://localhost:3000)
  - Default login: `admin` / `admin`
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Loki**: [http://localhost:3100](http://localhost:3100)
- **Tempo**: [http://localhost:3200](http://localhost:3200)

### 4. Load Testing
To generate traffic and see metrics/logs/traces:
```sh
python load_test.py
```

## File Explanations

### `main.py`
Contains the FastAPI application. It exposes endpoints and is instrumented for metrics, logging, and tracing.

### `load_test.py`
A script to send concurrent requests to the FastAPI app for testing monitoring and observability.

### `docker-compose.yml`
Defines all services: FastAPI app, Prometheus, Grafana, Loki, Tempo, and Promtail. Handles networking and volumes.

### `prometheus.yml`
Prometheus configuration for scraping metrics from the FastAPI app.

### `promtail-config.yml`
Promtail configuration for collecting and shipping logs to Loki.

### `tempo-config.yaml`
Tempo configuration for collecting distributed traces.

### `logs/app.log`
Application log file written by the FastAPI app and tailed by Promtail.

## Monitoring Stack Overview

- **Prometheus** scrapes metrics from FastAPI (e.g., request count, latency).
- **Grafana** visualizes metrics, logs, and traces. Dashboards can be created for real-time monitoring.
- **Loki** collects logs from the FastAPI app via Promtail.
- **Tempo** collects distributed traces from the FastAPI app.
- **Promtail** tails the log file and ships logs to Loki.

## Customization
- Add more endpoints to `main.py` as needed.
- Update `prometheus.yml` to scrape additional targets.
- Modify `promtail-config.yml` to collect more logs.
- Adjust `tempo-config.yaml` for advanced tracing setups.

## Useful Links
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Loki](https://grafana.com/oss/loki/)
- [Tempo](https://grafana.com/oss/tempo/)

