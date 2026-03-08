import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def save_context(session_id, data):
    redis_client.set(session_id, data)

def get_context(session_id):
    return redis_client.get(session_id)