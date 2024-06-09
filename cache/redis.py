import redis
import json
from conf import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def save_chat(queue_name, item):
    r.lpush(queue_name, json.dumps(item))


def get_chat(queue_name):
    item = r.rpop(queue_name)
    if item:
        return json.loads(item)
    return None


# Example usage
if __name__ == "__main__":
    queue_name = 'my_queue'
    cache_key = 'my_cache'

    # Add items to the queue
    save_chat(queue_name, {'id': 1, 'message': 'Hello, World!'})
    save_chat(queue_name, {'id': 2, 'message': 'Another message'})

    # Get items from the queue
    print("Dequeue item:", get_chat(queue_name))
    print("Dequeue item:", get_chat(queue_name))