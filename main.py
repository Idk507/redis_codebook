from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import shortuuid
from redis_db import redis

app = FastAPI()

class URLRequest(BaseModel):
    long_url: HttpUrl

BASE_HOST = "http://short.ly/"  # Base domain for short URLs

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = shortuuid.uuid()[:6]  # 6-char unique ID
    redis.set(short_code, request.long_url)
    return {"short_url": BASE_HOST + short_code}

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    long_url = redis.get(short_code)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": long_url}
