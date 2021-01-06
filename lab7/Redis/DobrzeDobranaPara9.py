# Nasłuchiwanie na każdą zmianę klucza wynikającą z komend 
# dedykowanych stringowi:
"""
from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
redis_connection.config_set('notify-keyspace-events','K$')
pub_sub = redis_connection.pubsub()
pub_sub.subscribe('__keyspace@0__:test_key')

for message in pub_sub.listen():
    print(message)
"""

from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
redis_connection.config_set('notify-keyspace-events','E$')
pub_sub = redis_connection.pubsub()
pub_sub.subscribe('__keyevent@0__:set')

for message in pub_sub.listen():
    print(message)