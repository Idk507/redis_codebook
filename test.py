import httpx
import time

start = time.time()
response = httpx.get("http://127.0.0.1:8000/expensive-computation")
print(response.json())
print("Time taken:", time.time() - start)
