# Podstawowe użycie typu danych o nazwie Strumienie
from redis import Redis
"""
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1)
print(message)

# Doda do strumienia słownik i odczyta z niego, podaną w parametrze count ilość elementów. 
# Nazwa strumienia do którego się podłączamy to słownik, którego kluczem
# jest nazwa strumienia, a wartością jest ID od którego chcemy dane odczytywać. 
# W tym przypadku – od początku.
"""
"""
# Teraz co 10 milisekund otrzymamy pustą tablicę 
# ponieważ teraz czekamy tylko na nowe dane, dodane do strumienia 
# bez wyświetlania tych wcześniejszych
# nawet po usunięciu z bazy danych
while True:
    message = redis_connection.xread({stream_name: '$'}, block=10, count=1)
    print(message)

"""

"""
# Poprawne odbieranie danych ze strumienia
# Kolejne powinny zawierać ID ostatnio odczytanej wiadomości.
# Jeśli nie zrobimy tego, to wiadomości wysłane pomiędzy 
# jednym blokowaniem a drugim – będą nam ginąć.
redis_connection = Redis(decode_responses=True, db=0)
stream_name ='testowy_strumien'
starting_point ="$"

while True:
    message = redis_connection.xread({stream_name: starting_point},
     block=10, count=1)
    if message:
        message = message[0][1][0]
        msg_id = message[0]
        msg_payload = message[1]
        starting_point = msg_id
        print(msg_payload, msg_id)
"""

# Poprawne odbieranie elemntów ze 
# strumienia oraz po potwierzedniu przetworzenia usnięcie
from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
stream_name ='testowy_strumien'
starting_point ="$"

while True:
    message = redis_connection.xread({stream_name: '0-0'}, 
    block=None, count=5)
    print(message)
    message = redis_connection.xread({stream_name: starting_point}, 
    block=10, count=1)
    if message:
        message = message[0][1][0]
        msg_id = message[0]
        msg_payload = message[1]
        starting_point = msg_id
        redis_connection.xdel(stream_name, msg_id)
        print(msg_payload, msg_id)
        message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1)
        print(message)


