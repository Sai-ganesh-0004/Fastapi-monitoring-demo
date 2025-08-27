from fastapi import FastAPI
import time
import random
import logging
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse

# ---------------------------------------------------
# Setup FastAPI
# ---------------------------------------------------
app = FastAPI()

# ---------------------------------------------------
# Setup Prometheus metrics
# ---------------------------------------------------
REQUEST_COUNT = Counter("request_count", "Total number of requests", ["endpoint"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency of requests", ["endpoint"])

# ---------------------------------------------------
# Setup logging
# ---------------------------------------------------
# Log file path (important: inside /var/log so Promtail can scrape it)
logging.basicConfig(
    filename="F:\\computer\\fastapi-monitoring-demo\\logs\\app.log",   # <-- changed from logs/app.log
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------
# Endpoints
# ---------------------------------------------------
@app.get("/")
def read_root():
    start_time = time.time()

    # simulate some work with random latency
    time.sleep(random.uniform(0.1, 0.5))

    latency = time.time() - start_time
    REQUEST_COUNT.labels(endpoint="/").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(latency)

    # Log each request
    logging.info("Handled request to / in %.3f seconds", latency)

    return {"message": "Hello, monitoring world!"}


@app.get("/log")
def log_example():
    # Example log endpoint
    logging.info("This is a log message from /log endpoint")
    return {"status": "logged"}


@app.get("/metrics")
def metrics():
    # Expose Prometheus metrics
    return PlainTextResponse(generate_latest().decode("utf-8"))
