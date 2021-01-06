from redis import Redis

#Dodawanie/Odejmowanie wartości od typu liczbowego
redis_connection = Redis(decode_responses=True)

key ="Obliczenia"
value =1300
redis_connection.set(key, value)
print(redis_connection.get(key))
print(redis_connection.incr(key,25))
print(redis_connection.decr(key,30))