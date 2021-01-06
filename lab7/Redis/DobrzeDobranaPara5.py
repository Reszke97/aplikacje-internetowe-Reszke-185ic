# Implementacja w Redisie

from redis import Redis

# Kanał komunikatów, wspomniany w poprzednim rozdziale,
# w redisie jest po prostu pewnym kluczem. 
# Załóżmy, że w poniższym przykładzie będzie to klucz 
# o nazwie „testowy_kanal_komunikacyjny”. 
# Napiszmy subskrybenta:

redis_connection = Redis(decode_responses=True)
pubsub = redis_connection.pubsub()
pubsub.subscribe("testowy_kanal_komunikacyjny")

for message in pubsub.listen():
    print(message)
#Po uruchomieniu tego kawałka kodu nasz subskrybent 
# odbiera pierwszą wiadomość, tzw. powitalną, informującą, 
# że się podłączyliśmy.