# Redis z Lua

"""
# Wykonanie komendy EVAL przekazując do niej skrypt z Lua
from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
#script ="""
#return "test"
"""
# drugi argument po script (tutaj 0) 
# określa ilość argumentów które można przekazać do skryptu.
print(redis_connection.eval(script,0))
"""

"""
# Określamy tutaj że dwa pierwsze 
# parametry będą dostępne w skrypcie 
# w tabeli KEYS a kolejne – w tabeli ARGV. 
# Sam skrypt odczytuje przekazane dane i zwraca je jako tablicę.
from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)

script ="""
#return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
"""

print(redis_connection.eval(script,2,1,2,'first','second'))
"""
"""
# Wygenerowanie liczb wewnątrz Lua:

from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)

script ="""
#local arr = {}
#for i = 0, 10 do
#    arr[i] = i
#end
#return arr
"""
print(redis_connection.eval(script,0))# lista od 1 do 10
"""

"""
# Lua z JSON'em
from redis import Redis
from json import dumps

redis_connection = Redis(decode_responses=True, db=0)

script ="""
#local json_data = KEYS[1]
#local decoded_data = cjson.decode(json_data)
#return decoded_data['a'] + decoded_data['b']
"""
print(redis_connection.eval(
    script,1, dumps({'a': 1,'b': 6})))  # wynik to 7
"""
"""
# Pobranie z Redisa i przetworzenie i zapisanie wyniku

from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
redis_connection.set("key1",10)

script ="""
#local arg1 = redis.call('get','key1')
#redis.call('set', 'key2', arg1 + KEYS[1])
#return nil
"""

print(redis_connection.eval(script,1,5))# None, ze względu na "return nil"
print(redis_connection.get("key2"))  # 15, bo 10 + 5 = 15
"""

# Pobranie z Redisa i przetworzenie i zapisanie wyniku cd.

from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
permission ='ADD_BOOKING' # <---- nazwa uprawnienia
redis_connection.sadd("users_group:2", *list(range(0,50))) #<------ nazwa i zakres grupy
redis_connection.sadd('permissions', permission) # <-- stworzenie uprawnien
# dotąd jest przygotowanie danych

add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""
# Pobranie z Redisa i przetworzenie i zapisanie wyniku cd.

from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
permission ='ADD_BOOKING' # <---- nazwa uprawnienia
redis_connection.sadd("users_group:2", *list(range(0,50))) #<------ nazwa i zakres grupy
redis_connection.sadd('permissions', permission) # <-- stworzenie uprawnien
# dotąd jest przygotowanie danych

add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""
# Powyższy skrypt możemy zapisać w Redisie i wywoływać go tak jak w lini 120 i 121
# sha= redis_connection.script_load(add_permission_script)
# print(redis_connection.evalsha(sha,2,2, permission))
print(redis_connection.eval(add_permission_script,2,2, permission))

# Dodanie konkretnych uprawnienień wszystkim użytkownikom którzy są w zadanej grupie.