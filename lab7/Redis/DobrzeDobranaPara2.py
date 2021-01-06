from redis import Redis

#Tworzenie pary klucz i wartosc ktora zwroci odpowiedz jako
#ciag bajtow
redis_connection = Redis()
key ="test"
value ="hello world!"
redis_connection.set(key, value)
print(redis_connection.get(key))