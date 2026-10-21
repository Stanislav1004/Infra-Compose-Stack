import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis

app = FastAPI(title="DevOps Stack App")

# Додаємо CORS, щоб фронт міг нормально стукатись до бека
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключаємося до Redis за назвою сервісу в Docker Compose
redis_host = os.getenv("REDIS_HOST", "cache")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/")
def read_root():
# Збільшуємо лічильник відвідувань у Redis при кожному запиті
    count = r.incr("hits")
    return {
        "status": "success",
        "message": "Welcome to the DevOps Stack Production App!",
        "visits": count
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
