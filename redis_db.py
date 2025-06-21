from redis import Redis

# Initialize Redis client
redis = Redis(host='localhost', port=6379, decode_responses=True)
