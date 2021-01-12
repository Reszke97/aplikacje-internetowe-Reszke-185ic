# Django + React + Crud

# Przerobiłem tutorial ze strony : https://bezkoder.com/django-react-axios-rest-framework/

# Wzbogaciłem projekt o uploadowanie zdjęcia oraz zmodyfikowałem stronę **Home**. Aby to osiągnąć konieczne było napisanie własnych views'ów oraz route'ów, co pokaże niżej w kodzie i na stronie.

# Tworzenie Backendu:

## Po przygotowaniu środowiska wirtualnego i zainstalowaniu Django instalujemy **Rest Framework** komendą:
```python
    pip install djangorestframework
```

## Następnie tworzymu aplikacje tutorials :
```python
python manage.py startapp tutorials
```
## Następnie w installed apps w pliku settings dodajemy:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django REST framework #<-------------------- rest framework
    'rest_framework',
    # Tutorials application 
    'tutorials.apps.TutorialsConfig',#<-------------- nazwa apki
]
```

## Następnie instalujemy następujący pakiet:
```python
pip install django-cors-headers
```

## Po tym w installed apps dodajemy:
```python
INSTALLED_APPS = [
    ...
    # CORS
    'corsheaders',
]
```

## Następnie do Middleware dodajemy:
```python
MIDDLEWARE = [
    # CORS
    'corsheaders.middleware.CorsMiddleware',#<-----------------tu
    'django.middleware.common.CommonMiddleware',#<-------------tu
    # Django Standard Middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## Trzeba również ustawić następujący kod:
```python
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)
```

## Teraz tworzenie modeli. Tak przedstawia się mój zmodyfikowany plik models:
```python
from django.db import models

# Tutaj musiałem zdefiniować metodę upload_path która będzie odpowiedzialna za zapisywanie wysłanego miejsca do podanej niżej scieżki
# Folderem nadrzędnym jest Folder media potem następny folder to cover następnie zostaje tworzony nowy folder title pobierany z tytułu danego tutoriala
# Na koniec do ostatniego folderu zostanie zapisane zdjęcie a nazwą tego zdjęcia będzie jego pierwotna nazwa
def upload_path(instance, filename):
    return '/'.join(['covers',str(instance.title),filename])

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    upload = models.ImageField(blank=True, null=True, upload_to=upload_path)#<----------- w bazie danych będą przechowywane zdjęcia, 
                                                                            #upload to jest odpowiedzialne gdzie zdjęcie zostane napisane

```

## Ważna rzecz to dodanie po tym w pliku settings.py następującego kodu:

```python
# Należy utowrzyc scieżkę do zdjęć
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'
```

## Następnie tworzenie serializerów. Tak przedstawia się zmodyfikowany Serializer:
```python
from rest_framework import serializers 
from tutorials.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'upload',#<-------- Podaje informacje że upload czyli zdjęcie również ma być uwzględnione
                )
```

## Następnie tworzenie Views'ów . Stworzyłem własne viewsy gdyż było to konieczne aby przesłać zdjęcie ponieważ przy kodzie z tutorial występował problem z **JsonParserem**.
## Wymagane było użycie **MultiPartParesra** oraz dodatkowo przekazanie danych za pomocą biblioteki axios jako:

```python
'content-type': 'multipart/form-data'
```
## Aby zdjęcie było dodane konieczna była zarówno zmiana backendu jak i frontendu. Tak przedstawiają sie moje viewsy:

```python
from django.shortcuts import render
from rest_framework import status
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import renderers
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Konieczne było przejście na Class view w przecziwnym wypadku Parser nie działał jak powninien
class TutorialView(APIView):
    parser_classes = (MultiPartParser, FormParser)#<---------- Tutaj wybieram parser

    # Aby była możliwość pobierania tutoriali z bazy na frontend należało zdefiniować metodę get,post,delete
    def get(self, request, *args, **kwargs):
        posts = Tutorial.objects.all()
        serializer = TutorialSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = TutorialSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        count = Tutorial.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Dodatkowo aby móc zedytować konkretny tutorial na stronie w react'cie lub na API należało zdefiniować metodę TutorialDetail
class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

```

## Po tym należało odpowiednio skonfigurować route'y co zrobiłem:
```python
from django.conf.urls import url 
from tutorials import views 
from django.urls import path
from .views import PostDetail
urlpatterns = [ 
    path('api/tutorials', views.PostView.as_view(), name= 'posts_list'),#<------- scieżka do API
    path('api/tutorials/<int:pk>/', PostDetail.as_view()),#<---------scieżka do konkretnego tuoriala w API
]
```

## Tak przedstawia się widok DRF Api dla listy wszystkich tutoriali:
![](1)

## Tak wygląda widok dla TutorialDetail:
![](2)

## Można standardowo wyświetlić dane w postaci JSON:
![](3)

# Tworzenie Frontendu:

## Zaczynamy od tworzenia Reacta na tym saym poziomie w drzewie folderów co środowisko wirtualne komendą:
```
npx create-react-app react-crud
```

## Następnie instalacja następujących pakietów:
```javascript
npm install bootstrap .// <--------- bootstrap konieczny do stylów z tutoriala
npm install --save react-router-dom .// <--------- potrzebne do Router'ów
npm install @material-ui/core//<--------- korzystałem z material ui do edycji strony Home
npm install axios.// <--------- biblioteka do obsługi wywołań asynchronicznych i przesyłania danych między back endem a fron endem
```

# Najważniejsze zmiany w Reacie:
```javascript
import axios from "axios";

export default axios.create({
  baseURL: "http://127.0.0.1:8080/api",
  headers: {
    'content-type': 'multipart/form-data'//<----------- Jak wspomniałem wcześniej należy zmienić content-type na multipart/form-data
  }
});
```
## Dodałem komponent funkcyjny **home.component.js** tak sie prezentuje:

```javascript
// Wykorzystałem material ui i na Box'ie stworzyłem zawartość strony przy wykorzystaniu Listy oraz TypoGraphy z Material UI
import React, { Component } from "react";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Typography from '@material-ui/core/Typography';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';
import Box from '@material-ui/core/Box';

export default function Home(){
    return (
    <div align="center">
        <Box
        boxShadow={2}
        bgcolor="background.paper"
        m={1}
        p={1}
        style={{ width: '50%',marginTop:'3rem'}}
      >
        <List>
                <ListItem >
                    <ListItemText
                        primary={
                        <Typography fontWeight="fontWeightBold" variant="h5">
                            <b>Django + React (aplikacja CRUD)</b>
                        </Typography>
                        }
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="frontend napisany za pomocą React.js,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="biblioteka ‘axios’ użyta do “konsumowania” API wystawionego np. przez DRF,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="przykład aplikacji CRUD z wykorzystaniem Django i React’a,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="należy przeanalizować i wdrożyć kod z ww. poradnika,"
                    />
                </ListItem>
                <ListItem >
                    <ListItemIcon>
                        <FiberManualRecordIcon/>
                    </ListItemIcon>
                    <ListItemText
                        primary="plusy za własne przemyślenia, analizę dokumentacji i idące za nimi modyfikacje w aplikacji."
                    />
                </ListItem>
            </List>
      </Box>
    </div>
    );
}
```

## Zmodyfikowany pli App.js:

```javascript
import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Switch, Route, Link } from "react-router-dom";
import "./App.css";

import AddTutorial from "./components/add-tutorial.component";
import Tutorial from "./components/tutorial.component";
import TutorialsList from "./components/tutorials-list.component";
import Home from "./components/home.component";

class App extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand navbar-dark bg-primary">
          <a href="/" className="navbar-brand">
            Home
          </a>
          <div className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link to={"/tutorials"} className="nav-link">
                Tutorials
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/add"} className="nav-link">
                Add
              </Link>
            </li>
          </div>
        </nav>

        <div className="container mt-3">
          <Switch>
            <Route exact path={["/"]} component={Home} />              <!-- Tutaj zamiast jako stronę startową tutorials ustawiłem Home-->
            <Route exact path={["/tutorials"]} component={TutorialsList} />
            <Route exact path="/add" component={AddTutorial} />
            <Route path="/tutorials/:id" component={Tutorial} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;
```

## Dodanie zdjęcia z poziomu Reacta czyli zmiana w komponencie **add-tutorial.component.js**:

```javascript
import React, { Component } from "react";
import Buttons from '../services/Buttons'
import axios from "axios";

export default class AddTutorial extends Component {
  constructor(props) {
    super(props);
    this.onChangeTitle = this.onChangeTitle.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.saveTutorial = this.saveTutorial.bind(this);
    this.newTutorial = this.newTutorial.bind(this);
    this.onChange = this.onChange.bind(this); // dodanie binda do funkcji

    this.state = {
      id: null,
      title: "",
      description: "", 
      published: false,
      upload: [],//<------------- dodałem tutaj atrybut upload do przekazywania zdjęcia
      submitted: false,
      image: null,// <-------- dodałem tutaj atrybut image który będzie służył do wyświetlenia aktualnie wybranego zdjęcia na stronie
    };
  }


  onChangeTitle(e) {
    this.setState({
      title: e.target.value
    });
  }

  onChangeDescription(e) {
    this.setState({
      description: e.target.value
    });
    console.log(this.state)
  }


/*Całkowicie musiałem zmienić funkcję saveTutorial aby przekazywała da Axiosa dane w postaci FormData*/
  saveTutorial() {
      const formData = new FormData();// tworzenie nowego typu FormData i wypełnienie wszystkich niezbędnych kolumn w bazie danych
      formData.append("title", this.state.title);
      formData.append("description", this.state.description);
      formData.append("upload", this.state.upload, this.state.upload.name);

      axios.post("http://127.0.0.1:8080/api/tutorials", formData, {// tutaj bezpośrednio należało przekazać dane do api/tutorials
        headers: {
          'content-type': 'multipart/form-data'
        } 
    });
      this.setState({ // po poprawnym wysłaniu danych status submitted ustawiam na true aby wyświetlił się komunikat odpowiedni
        submitted:true
      })
  }
 
  newTutorial() {
    this.setState({
      id: null,
      title: "",
      description: "",
      published: false,
      //here
      upload: null,
      image: null,
      submitted: false
    });
    console.log(this.state.file)
  }

  onChange = e => { // Nowa funkcja która odpowiada za wczytanie zdjęcia
    console.log(this.state.file)
    const files = Array.from(e.target.files) //pobranie zdjęcia
    this.setState({
      upload: files[0], // przypisanie do atrybutu upload zdjęcia
      image: URL.createObjectURL(e.target.files[0])// wyświetlenie aktualnie wybranego zdjęcia na stronie
    });
  }

  render() {
    return (
      <div className="submit-form">
        {this.state.submitted ? (
          <div>
            <h4>You submitted successfully!</h4>
            <button className="btn btn-success" onClick={this.newTutorial}>
              Add
            </button>
          </div>
        ) : (
          <div>
            <div className="form-group">
              <label htmlFor="title">Title</label>
              <input
                type="text"
                className="form-control"
                id="title"
                required
                value={this.state.title}
                onChange={this.onChangeTitle}
                name="title"
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Description</label>
              <input
                type="text"
                className="form-control"
                id="description"
                required
                value={this.state.description}
                onChange={this.onChangeDescription}
                name="description"
              />
            </div>

            <div className="form-group">
              <Buttons onChange={this.onChange} /><!--            Tutaj po naciśnięciu załadowanie zdjęcia            -->
              <img src={this.state.image}/>
            </div>

            <button onClick={this.saveTutorial} className="btn btn-success">
              Submit
            </button>
          </div>
        )}
      </div>
    );
  }
}
```

## W folderze services stworzyłem Plik Buttons.js, w którym zdefiniowałem guzik do przesyłania zdjęcia:

```javascript
import React from 'react'

export default props => 
  <div className='buttons fadein'>
    
    <div className='button'>
      <label htmlFor='single'>
      </label>
      <input type='file' id='single' onChange={props.onChange} /> 
    </div>

  </div>
```

## Do wyświetlenia listy tutoriali wystarczyło dodać te linie kodu w pliku tutorials-list.component w return'ie:
```javascript
<div>
    <label>
        <strong>zdjecie:</strong>
    </label>{" "}
    {currentTutorial.upload}
</div>
```

## Do edycji poszczególnych tutoriali należało również zedytować funkcje w komponencie tutorial.component.js . Kod prezentuje się następująco:
```javascript
import React, { Component } from "react";
import TutorialDataService from "../services/tutorial.service";
import Buttons from '../services/Buttons'
import axios from "axios";

export default class Tutorial extends Component {
  constructor(props) {
    super(props);
    this.onChangeTitle = this.onChangeTitle.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.getTutorial = this.getTutorial.bind(this);
    this.updatePublished = this.updatePublished.bind(this);
    this.updateTutorial = this.updateTutorial.bind(this);
    this.deleteTutorial = this.deleteTutorial.bind(this);
    this.onChange = this.onChange.bind(this);

    this.state = {
      currentTutorial: {
        id: null,
        title: "",
        description: "",
        published: false,

        //here <--------------------- utorzenie atrubutów upload i image
        upload: [],
        image: null,

      },
      message: ""
    };
  }

  componentDidMount() {
    this.getTutorial(this.props.match.params.id);
  }
  onChange = e => {
    const files = Array.from(e.target.files)
    console.log(files)
    this.setState({
      upload: files[0],
      image: URL.createObjectURL(e.target.files[0])
    });
  }

  onChangeTitle(e) {
    const title = e.target.value;

    this.setState(function(prevState) {
      return {
        currentTutorial: {
          ...prevState.currentTutorial,
          title: title
        }
      };
    });
  }

  onChangeDescription(e) {
    const description = e.target.value;
    
    this.setState(prevState => ({
      currentTutorial: {
        ...prevState.currentTutorial,
        description: description
      }
    }));
  }

  getTutorial(id) {
    TutorialDataService.get(id)
      .then(response => {
        this.setState({
          currentTutorial: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updatePublished(status) { //<-------------------     tutaj należało zmodyfikować typ danych przekazywany do bazy danych na FormData i przekazać go jako 2 argument to funkcji
    var data = {//Należało utworzyć obiekt data który będzie zawierał aktualny status a następnie przekazanie go do formData w append'dzie
      published: status,
    };
    const formData = new FormData()
    formData.append("id",this.state.currentTutorial.id)
    formData.append("title",this.state.currentTutorial.title)
    formData.append("description",this.state.currentTutorial.description)
    formData.append("published",data.published)
    formData.append("upload",this.state.upload, this.state.upload.name )

    TutorialDataService.update(this.state.currentTutorial.id, formData)// <-------------------- Przekazanie form data do funkcji, która wrzuca dane do backendu
      .then(response => {
        this.setState(prevState => ({
          currentTutorial: {
            ...prevState.currentTutorial,
            published: status
          }
        }));
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updateTutorial() {// <-------------------     tutaj należało zmodyfikować typ danych przekazywany do bazy danych na FormData i przekazać go jako 2 argument to funkcji
      const formData = new FormData();
      console.log(this.state.upload)
      console.log(this.state.upload.name)
      formData.append("title", this.state.currentTutorial.title);
      formData.append("description", this.state.currentTutorial.description);
      formData.append("upload", this.state.upload, this.state.upload.name);
    TutorialDataService.update(
      this.state.currentTutorial.id,
      formData // <-------------------- Przekazanie form data do funkcji, która wrzuca dane do backendu
    )
      .then(response => {
        console.log(response.data);
        this.setState({
          message: "The tutorial was updated successfully!"
        });
      })
      .catch(e => {
        console.log(e);
      });
  }

  deleteTutorial() {    
    TutorialDataService.delete(this.state.currentTutorial.id)
      .then(response => {
        console.log(response.data);
        this.props.history.push('/tutorials')
      })
      .catch(e => {
        console.log(e);
      });
  }

  render() {
    const { currentTutorial } = this.state;

    return (
      <div>
        {currentTutorial ? (
          <div className="edit-form">
            <h4>Tutorial</h4>
            <form>
              <div className="form-group">
                <label htmlFor="title">Title</label>
                <input
                  type="text"
                  className="form-control"
                  id="title"
                  value={currentTutorial.title}
                  onChange={this.onChangeTitle}
                />
              </div>
              <div className="form-group">
                <label htmlFor="description">Description</label>
                <input
                  type="text"
                  className="form-control"
                  id="description"
                  value={currentTutorial.description}
                  onChange={this.onChangeDescription}
                />
              </div>

              <div className="form-group">
                <label htmlFor="zdjecie">zdjecie</label>
                <Buttons onChange={this.onChange} />            <!-- Tutaj dodałem zmiane zdjęcie-->
              <img src={this.state.image}/>
              </div>

              <div className="form-group">
                <label>
                  <strong>Status:</strong>
                </label>
                {currentTutorial.published ? "Published" : "Pending"}
              </div>
            </form>

            {currentTutorial.published ? (
              <button
                className="badge badge-primary mr-2"
                onClick={() => this.updatePublished(false)}
              >
                UnPublish
              </button>
            ) : (
              <button
                className="badge badge-primary mr-2"
                onClick={() => this.updatePublished(true)}
              >
                Publish
              </button>
            )}

            <button
              className="badge badge-danger mr-2"
              onClick={this.deleteTutorial}
            >
              Delete
            </button>

            <button
              type="submit"
              className="badge badge-success"
              onClick={this.updateTutorial}
            >
              Update
            </button>
            <p>{this.state.message}</p>
          </div>
        ) : (
          <div>
            <br />
            <p>Please click on a Tutorial...</p>
          </div>
        )}
      </div>
    );
  }
}
```
## Po dokonaniu powyższych modyfikacji tak prezentuje się strona:

# Widok Strony Home:

![](4)

## Tworzenie nowego Tutoriala:
![](5)

## Po dodaniu tutoriala pojawia się komunikat:
![](6)

## Na zdjęciu poniżej widać że dodano tutorial(nie wyświetlam zdjęć na stronie są one zapisywane w folderze **media**):
![](7)

## Edycja istniejącego tutoriala:
![](8)

## Komunikat o pomyślnym zaktualizowaniu zdjęcia:
![](9)

## Jak widać na poniższym zdjęciu udało się zedytować tutorial(zedytowałem zdjęcie co jest odwzorowane w nazwie):
![](10)

## Na poniższym zrzucie widać że w pliku media/covers/Test znajdują się zdjęcia(po wykonaniu publish zdjęcie zostaje tam dodane tak jak po wykonaniu update więc są 2 razy tes same):
![](11)

## Po kliknięciu w edit i kiknięciu delete tutorial zostanie usunięty:
![](12)

## Po dodaniu przykładowych tutoriali i kliknięciu delete wszystkie zostaną usnięte:
![](13)

## Jak widać tutoriale zostały usunięte.
![](14)

# Do wykonania zadania pomcne były poniższe artykuły:
- https://medium.com/@emeruchecole9/uploading-images-to-rest-api-backend-in-react-js-b931376b5833
- https://medium.com/@650egor/react-30-day-challenge-day-2-image-upload-preview-2d534f8eaaa
