from redis import Redis

#Tworzenie pary klucz, wartosc gdzie zwraca nam string
redis_connection = Redis(decode_responses=True)  # <- tu zmiana!
key ="test2"
value ="hello world again!"
redis_connection.set(key, value)
print(redis_connection.get(key))