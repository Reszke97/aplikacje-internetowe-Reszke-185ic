from redis import Redis

#Hashe

#Czyli po prostu mapy. Słowniki. 
# Tablice asocjacyjne. 
# Nazw jest dużo, ale idea ta sama – struktura danych 
# przechowująca klucze i odpowiadające im wartości.

redis_connection = Redis(decode_responses=True)
hash_key ='test_hash'
redis_connection.hset(hash_key,'key','value')
redis_connection.hset(hash_key,'key2','value2')

# Powyższy kawałek kodu pozwala 
# na stworzenie pod kluczem „test_hash” właśnie słownika,
# który będzie miał dwa klucze „key/key2” 
# o wartości „value/value2”