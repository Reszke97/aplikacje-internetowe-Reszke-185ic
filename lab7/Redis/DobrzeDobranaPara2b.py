from redis import Redis

#Dołączanie do istniejącej wartości stringa
redis_connection = Redis(decode_responses=True)
key ="test2"
value ="hello world again!"
redis_connection.set(key, value)
print(redis_connection.get(key))
redis_connection.append(key," Redis Test101")
print(redis_connection.get(key))

#Usunięcie istniejącego klucza i wartości
redis_connection.delete(key)
print(redis_connection.get(key))