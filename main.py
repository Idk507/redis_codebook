from fastapi import FastAPI
from redis import Redis
import time

app = FastAPI()

# Connect to Redis (default port is 6379)
redis_client = Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/expensive-computation")
def expensive_computation():
    cache_key = "expensive_result"

    # Check Redis cache
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return {"result": cached_result, "source": "cache"}

    # Simulate long-running process
    time.sleep(5)
    result = "Expensive result at " + time.strftime("%X")

    # Store in Redis with a timeout (TTL of 10 seconds)
    redis_client.setex(cache_key, 10, result)

    return {"result": result, "source": "calculated"}
