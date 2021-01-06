from redis import Redis

"""
#Tworzenie listy
redis_connection = Redis(decode_responses=True)
list_key ="Pierwsza lista w Redisie"
redis_connection.rpush(list_key,1,2,3,4,5)
print(redis_connection.lrange(list_key,0, -1))
"""

"""
#Tworzenie listy oraz jej wyświetlenie w podanym przedziale
redis_connection = Redis(decode_responses=True)
list_key ="Pierwsza lista w Redisie"
redis_connection.rpush(list_key,10,20,30,40,50)
print(redis_connection.lrange(list_key,1,3))
"""

#Metoda blokująca wykonywanie programu(brpop)
redis_connection = Redis(decode_responses=True)
list_key ="example-list"
whileTrue:print(redis_connection.brpop(list_key))

# Ten program, po uruchomieniu, działa cały czas. 
# Wywołanie BRPOP skutkuje blokadą programu, 
# jeśli w liście nie ma elementów. 
# Jeśli są, to pobiera ostatni element, 
# a w przypadku programu wyżej, zapętla się, 
# pobierając wszystkie elementy i po ostatnim – blokuje program.