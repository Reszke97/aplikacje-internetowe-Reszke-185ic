# Czat z użyciem Web Socket + Web Workers. Wykorzystałem Django-Channels oraz przerobiłem inny przykład ponieważ miałem problem z przerobieniem przykładu https://medium.com/@ksarthak4ever/django-websockets-and-channels-85b7d5e59dda więc przerobiłem i wdrożyłem następujący przykład:https://channels.readthedocs.io/en/stable/tutorial/part_1.html.


## Standardowo najpierw tworzymy środowisko wirtualne, instalujemy django i tworzymy aplikacje. Następnie należy zainstalować Django-channels:
```py
pip install channels
```
## Dodajemy utworzone aplikacje oraz channels do pliku settings.py:
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'ChannelsImplementation',
]
```

## Należy również zainstalować channel_redis do implementacji channels'ów:
```py
pip install channels_redis
```

## Następnie należy powiedzieć Django o tym że będziemy używać ASGI(Asynchronous Service Gateway Interface) czyli z operacji asynchronicznych w Django podajemy scieżke do pliku ASGI.py:
```py
ASGI_APPLICATION = 'ChannelsExample.asgi.application'
```
## Należy również zdefiniować w pliku settings.py ustawienia dla channelsów. Używany będzie Redis jako Backend. O to opcje które należy dodać:
```py
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

## Należy także w pliku ASGI.py podać informację że będziemy korzystać z Channels:

```py
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import ChannelsImplementation.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChannelsExample.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ChannelsImplementation.routing.websocket_urlpatterns
        )
    ),
})
```
## Następnie można utworzyć widoki/urlsy/szablony. Tak przedstawiają sie moje widoki:
```py
# chat/views.py
from django.shortcuts import render

def create_room(request):# -----------> Stworzony widok stworzenia pokoju chatu
    return render(request, 'chat/create_room.html')

def chat_room(request, room_name):# ---------------> Stworzony widok, w którym możliwa jest opcja chatu
    return render(request, 'chat/room.html', {'room_name': room_name})

def home(request):# -----------------> Stworzony widok home, dla strony głównej
    return render(request,'chat/home.html')

def fibonacci(request):# -----------------> Stworzony widok dla ciągu Fibonacciego korzystającego z Web Workera
    return render(request,'chat/fibonacci.html')

def factorial(request): # -----------------> Stworzony widok dla silini korzystającej z Web Workera
    return render(request,'chat/factorial.html')
```
## Urls:
```py
# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.create_room, name='index'),
    path('chat/<str:room_name>/', views.chat_room, name='room'),#tutaj po chat/ z szablonu gdzie podajemy roomName 
                                                                #jest on tu przekazywany i następnie zwracany w slowniku we viewsach wazne zeby zmienna tutaj po str: miala taka sama
                                                                # nazwe jak tak we viewsach w zwracanym slowniku inaczej serwer nie bedzie wiedzial na jakim kanale jestesmy
    path('',views.home, name='home'),
    path('fibonacci/',views.fibonacci, name='web_workers'),
    path('factorial/',views.factorial, name='factorial'),
]
```

## Należy również stworzyć plik consumers.py, który odpowiada za akceptacje wszystkich połączeń, odbioru wiadomości od swojego klienia odsyła je z powrotem do tego samego klienta. W przykładzie został użyty asynchroniczny konsument który jest bardziej wydajny niż synchroniczny konsument gdyż wchodzą tutaj w grę obliczenia wielowątkowe wykonane na serwerze.
## Gdy użytkownik publikuje wiadomość, funkcja JavaScript prześle wiadomość przez WebSocket do ChatConsumer. ChatConsumer otrzyma tę wiadomość i przekaże ją do grupy odpowiadającej nazwie pokoju. Każdy ChatConsumer w tej samej grupie (a więc w tym samym pokoju) otrzyma wiadomość od grupy i przekaże ją przez WebSocket z powrotem do JavaScript, gdzie zostanie dołączona do dziennika czatu.
```py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
```
## Musimy utworzyć konfigurację routingu dla aplikacji czatu, która ma trasę do konsumenta w tym celu tworzymy plik routing.py:
```py
# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
```

## Tak przedstawia się szablon w którym tworzony jest nowy pokój. W prosty sposób za pomocą ciasteczek dodatkowo dodałem nick użytkownika który będzie wyświetlany przy wysyłaniu wiadomości. Sposób ten nie jest dobrą praktyką ponieważ nie jest to bezpieczne przekazywać danę w ten sposób lecz na potrzeby laboratorium wykonałem to w taki sposób:
```html
{% extends 'chat/base.html' %}
{% block content %}
    <div class="paddingTopAfterNav" align="center">

        <form class="form">
            <div class="form-group">
                <label>What chat room would you like to enter?</label>
                <input type="text" class="form-control" id="room-name-input" placeholder="Enter room name" >
            </div>
            <div class="form-group">
                <label >What will be your nick name?</label>
                <input type="text" class="form-control" id="user-name-input" placeholder="Enter Nick Name"> <!-- Tutaj dodałem input z nazwą użytkownika -->
            </div>
            <button type="button" id="room-name-submit" class="btn btn-primary">Enter</button>
        </form>
        <script>
            document.querySelector('#room-name-input').focus();
            document.querySelector('#room-name-input').onkeyup = function(e) {
                if (e.keyCode === 13) {  // enter, return
                    document.querySelector('#room-name-submit').click();
                }
            };

            document.querySelector('#room-name-submit').onclick = function(e) {
                var roomName = document.querySelector('#room-name-input').value;
                var userName = document.querySelector('#user-name-input').value;
                document.cookie = userName;         // Tutaj tworzony jest cookie i przekazywany do niego user nick
                window.location.pathname = '/chat/' + roomName + '/';//tutaj tworzymy room name
            };

        </script>
    </div>
{% endblock %}
```

## Tak przedstawia się szablon w którym wyświetlany jest czat:
```html
{% extends 'chat/base.html' %}
{% block content %}
    <div class="paddingTopAfterNav" align="center">
        <p id="chat-log"style="white-space: initial;width:40%;height:45%;overflow-y:auto;border:solid;margin-top:3rem;border-color: white;color:white;text-align:left;position:relative;
        border-bottom:0px;padding-left:0.35rem;border-radius:0.55rem 0.55rem 0 0;border-color:gray;"class="style-1"></p>
        <!--<input id="chat-message-input" class="chatBox" type="text" size="100"><br>
        <input id="chat-message-submit" type="button"  value="Send" class="sendButton">-->
        <form class="form">
            <div class="form-group">
                <input type="text" class="form-control chatBox" id="chat-message-input" placeholder="Type message" >
            </div>
            <button type="button" id="chat-message-submit" class="btn btn-primary sendButton">Send</button>
        </form>

        {{ room_name|json_script:"room-name" }}  <!--stworzna tutaj została pętla w której pobieram user name z ciasteczka-->
        <script>
            var cookie = document.cookie;
            var userName = "";
            var temp ="";
            console.log(cookie)
            var test;
            for(var i = 0;i<cookie.length;i++){

                if(cookie.substr(i,1)==';'){
                    break;
                }
                temp = cookie.substr(i,1)
                userName=userName.concat(temp)
            }

            const roomName = JSON.parse(document.getElementById('room-name').textContent); // tutaj zostaje przekazana informacja o nazwie pokoju
            const chatSocket = new WebSocket(
                'ws://'
                + window.location.host
                + '/ws/chat/'
                + roomName
                + '/'
            );

            chatSocket.onmessage = function(e) { // tutaj otrzymywane sa dane z metodu chatSocket.send()
                const data = JSON.parse(e.data);
                document.querySelector('#chat-log').innerText += (data.message + '\n');
                test = document.querySelector('#chat-log').value
                console.log(test)
            };

            chatSocket.onclose = function(e) {
                console.error('Chat socket closed unexpectedly');
            };

            document.querySelector('#chat-message-input').focus();
            document.querySelector('#chat-message-input').onkeyup = function(e) {
                if (e.keyCode === 13) {  // enter, return
                    document.querySelector('#chat-message-submit').click();
                }
            };

            document.querySelector('#chat-message-submit').onclick = function(e) {
                const messageInputDom = document.querySelector('#chat-message-input');

                const message = userName+': '+messageInputDom.value;// tutaj do wiadomosci dodaje user name
                chatSocket.send(JSON.stringify({
                    'message': message
                }));
                messageInputDom.value = '';
            };
        </script>
    </div>
{% endblock %}
```

# Część 2 Web Workers:

## Tak przedstawia się szablon w którym korzystam z Web Workera do wylicznia wyrazów ciągu
```js
{% extends 'chat/base.html' %}
{% block content %}
    <div class="paddingTopAfterNav webWorkerMainDiv" align="center">
        <form>
            <div style="padding-top:1rem;">
                <h3>Fibonacci Sequence</h3>
                <input type="number" id="number" placeholder="Enter a number"style="padding:0.32rem;"> <!-- tutaj użytkownik może podać ile wyrazów ciągu obliczyć -->
                <button type="submit" class="btn btn-primary"style="transform:translate(-3%,-5%);">Enter</button>
            </div>
        </form>

        <div id="result" style="overflow-y:auto;height:500px;width:100%;"></div>
    </div>
    <script id="fibonacci" type="javascript/worker">
        self.onmessage = function(e) { // gdy zostaie wywoałany skrypt to na początku zostanie wywołana funkcja onmessage i następnie w niej wywołujemy funkcję fibonnaci
                                        // a w niej po dokonaniu obliczeń wywołujemy metode postMessage()
            let userNum = Number(e.data);
            fibonacci(userNum);
        }

        function fibonacci(number){
            let array =[];
            let variableA = 1, variableB = 0, temp,i=1;
            while (number >= 0){
                temp = variableA;
                variableA = variableA + variableB;
                variableB = temp;
                array.push(variableA)
                number--;
                if(i==1){
                    self.postMessage('First '+' number in the sequence '+ '= {'+array+'}');
                    i++;
                }
                else{
                    self.postMessage('First '+i+' numbers in the sequence '+ '= {'+array+'}');
                    i++;
                }
            }

        }
    </script>

    <script>
        var blob = new Blob([document.querySelector('#fibonacci').textContent]);// Tutaj następuje właściwe wywołanie workera i przekazanie do niego scieżki 
                                                                                //do skryptu js w którym jest zawarta cała logika i zwracane wartości
        blobURL = window.URL.createObjectURL(blob);
        var form = document.querySelector('form');
        var input = document.querySelector('input[type="number"]');
        var result = document.querySelector('div#result');
        var worker = new Worker(blobURL);

        worker.onmessage = function(event) { // tutaj po wykonaniu zadania zostają zwrócone wartości z workera i zostaje wykonane logika z tej części kodu
            var para = document.createElement("p");
            para.textContent = event.data;
            result.appendChild(para);
        };

        form.onsubmit = function(event) {// przekazanie wartości użytkownika do workera
            event.preventDefault();
            worker.postMessage(input.value);
            input.value = '';
        }
    </script>


{% endblock %}
```

## Tak przedstawia się szablon w którym korzystam z Web Workera do wylicznia silni:
```html
{% extends 'chat/base.html' %}
{% block content %}
    <div class="paddingTopAfterNav webWorkerMainDiv" align="center">
        <form>
            <div style="padding-top:1rem;">
                <h3>Factorial Calculation</h3>
                <input type="number" id="number" placeholder="Enter a number"style="padding:0.32rem;">
                <button type="submit" class="btn btn-primary"style="transform:translate(-3%,-5%);">Enter</button>
            </div>
        </form>

        <div id="result2" style="overflow-y:auto;height:500px;width:100%;"></div>
    </div>
    <script id="factorial" type="javascript/worker">
                                // Tutaj zawarty jest web Worker
        var factorial
        self.onmessage = function(e) {
            let userNumber = Number(e.data);
            factorial(userNumber);
        }

        function factorial(userNumber){
            var temp;
            factorial = userNumber;
            console.log(factorial)
            while (userNumber > 1){
                userNumber--;
                temp = factorial;
                factorial *= userNumber;
                self.postMessage(temp+'*'+userNumber+ '='+factorial);
            }
        }
    </script>

    <script>
        // tutaj wywołanie i poźniejsze akcje związane z web workerem
        var blob = new Blob([document.querySelector('#factorial').textContent]);
        blobURL = window.URL.createObjectURL(blob);
        var form = document.querySelector('form');
        var input = document.querySelector('input[type="number"]');
        var result = document.querySelector('div#result2');
        var worker = new Worker(blobURL);

        worker.onmessage = function(event) {
            var para2 = document.createElement("p");
            para2.textContent = event.data;
            result.appendChild(para2);
        };

        form.onsubmit = function(event) {
            event.preventDefault();
            worker.postMessage(input.value);
            input.value = '';
        }
    </script>
{% endblock %}
```
# Ważne aby uruchomić redisa bez niego komunikacja będzie niemożliwa.

# Front End:

## Tak przedstawia się strona Home:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/2.PNG)

## Tak przedstawia się strona na której tworzony jest pokój:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/3.PNG)

## Na poniższym zrzucie uruchomiłem 2 przeglądarki po lewej Edge a po prawej chrome i jak widać są ta 2 różne ciasteczka, które zostają tam dodane po wpisaniu nicku do inputa z wcześniejszej strony oraz widać ze komunikacja działa poprawnie i widać osoby, które ze sobą piszą:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/4.PNG)

## Tak przedstawia się ogólny widok czatu:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/5.PNG)

## Tak przedstawia się ciąg fibonacciego:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/6.PNG)

## Tak przedstawia się silnia:
![](https://github.com/Reszke97/aplikacje-internetowe-Reszke-185ic/blob/master/lab8/zrzuty/7.PNG)
