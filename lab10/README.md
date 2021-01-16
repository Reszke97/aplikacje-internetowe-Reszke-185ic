# Django + React (aplikacja typu ToDo)

# Przerobiłem tutorial ze strony : https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

## Wygląd strony:

## Wykorzystałem React Router połączony z Bootstrap NavBarem aby dodać jeszcze stronę **Home**

## Strona Home:
![](1)

## Strona Todo List:
![](2)


# Tworzenie Backendu:

## Najpierw tworzone jest środowisko wirtualne, następnie instalujemy Django i tworzymy aplikacje.

## Tworzenie modeli w pliku todo/models.py:

```python
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title
```

## Zarejestrowanie modeli do panelu administratora:
```python
# todo/admin.py

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Todo, TodoAdmin)
```

## Podczepienie API do naszej aplikacji. Do tego posłuży nam znowu DRF(Django Rest Framework):
```python
pip install djangorestframework django-cors-headers
```

## Należy zawsze pamiętać o tym aby dodać do pliku settings.py informacje o tym że korzystamy z DRF oraz o pakiecie CORS:
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',#<---------------Cors
    'rest_framework',#<--------------DRF
    'todo',
  ]
```

```py
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    #<------------ Cors
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## Teraz należy skorzystać z biblioteki Django-cors-headers i dodać do whitelist'y nasz serwer do frontendu czyli localhost:3000. Czyli dodać poni

```py
CORS_ORIGIN_WHITELIST = (
     'localhost:3000/'
 )
```

## Dodatkowo aby uniknąć błędów na etapie kompilacji kodu należy zmodyfikować kod do poniższej postaci:

```py
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
    'http://localhost:8080',
    'http://localhost:3000',
)
```

## Tworzenie serializer'ów w pliku todo/serializers.py:
```py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed') #<---- te pola mają być wyświetlane
```

## Tworzenie widoków:
```py
from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet): #<------------- Zdefiniowanie widoków W api(Post, Get, Delete, Post_Detail)
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()
```

## Zdefiniowanie scieżek w pliku backend\urls.py. Wykorzystanie Router'a:
```py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

# Tworzenie Frontendu W React'cie:

## Standardowo poniższą komendą tworzymy apkę w React'cie:

```js
npx create-react-app frontend
```

## Instalowanie bootstrapa, React Router, Material UI , Material UI Icons
```js
npm install @material-ui/icons
npm install @material-ui/core
npm install --save react-router-dom
npm install react-bootstrap bootstrap
npm install --save reactstrap react react-dom
```

## Stworzenie pliku z komponentami src\Modal.js:

```js
import React, { Component } from "react";
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Todo Item </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="title">Title</Label>
                  <Input
                    type="text"
                    name="title"
                    value={this.state.activeItem.title}
                    onChange={this.handleChange}
                    placeholder="Enter Todo Title"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Description</Label>
                  <Input
                    type="text"
                    name="description"
                    value={this.state.activeItem.description}
                    onChange={this.handleChange}
                    placeholder="Enter Todo description"
                  />
                </FormGroup>
                <FormGroup check>
                  <Label for="completed">
                    <Input
                      type="checkbox"
                      name="completed"
                      checked={this.state.activeItem.completed}
                      onChange={this.handleChange}
                    />
                    Completed
                  </Label>
                </FormGroup>
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Save
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }
```

## Modyfikacja index.js:
```js
// frontend/src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';       // add this
import './index.css';
import './myCss.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter } from "react-router-dom";

/*ReactDOM.render(<App />, document.getElementById('root'));
serviceWorker.unregister();*/

ReactDOM.render(
    <BrowserRouter>
      <App />
    </BrowserRouter>,
    document.getElementById("root")
);
serviceWorker.unregister();
```

## Modyfikacja skryptu App.js:
```js
import React, { Component } from "react";
import Modal from "./components/Modal";
import { Switch, Route, Link } from "react-router-dom";
import axios from "axios";
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';
import Box from '@material-ui/core/Box'
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Typography from '@material-ui/core/Typography';
import ListItemIcon from '@material-ui/core/ListItemIcon';


class App extends Component{
  render(){
    return(
      <div>
        <nav className="navbar navbar-expand navbar-light bg-light">
          <a href="/" className="navbar-brand">
            Home
          </a>
          <div className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link to={"/Tasks"} className="nav-link">
                Todo List
              </Link>
            </li>
          </div>
        </nav>

        <div className="container mt-3">
          <Switch>
            <Route exact path={["/"]} component={Home} />
            <Route exact path={["/Tasks"]} component={Lista} />
          </Switch>
        </div>
      </div>
    );
  }
}

function Home(){ // <---------------------------- Zdefiniowałem metodę Home, która bedzię wyświetlana jaka strona główna przy użyciu komponentów z Material UI
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
                      <b>Django + React (aplikacja typu ToDo)</b>
                  </Typography>
                  }
              />
          </ListItem>
          <ListItem >
              <ListItemIcon>
                  <FiberManualRecordIcon/>
              </ListItemIcon>
              <ListItemText
                  primary="backend napisany w Django,"
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
                  primary="przykład aplikacji To-Do z wykorzystaniem Django i React’a,"
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




class Lista extends Component { // Funkcja która tworzy podstronę ToDo List
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false
      },
      todoList: []
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/todos/")
      .then(res => this.setState({ todoList: res.data }))
      .catch(err => console.log(err));
  };
  displayCompleted = status => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };
  renderTabList = () => {
    return (
      <div className="my-5 tab-list">
        <span
          onClick={() => this.displayCompleted(true)}
          className={this.state.viewCompleted ? "active" : ""}
        >
          complete
        </span>
        <span
          onClick={() => this.displayCompleted(false)}
          className={this.state.viewCompleted ? "" : "active"}
        >
          Incomplete
        </span>
      </div>
    );
  };
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      item => item.completed === viewCompleted
    );
    return newItems.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2"
          >
            {" "}
            Edit{" "}
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete{" "}
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/todos/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/todos/", item)
      .then(res => this.refreshList());
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/todos/${item.id}`)
      .then(res => this.refreshList());
  };
  createItem = () => {
    const item = { title: "", description: "", completed: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button onClick={this.createItem} className="btn btn-primary">
                  Add task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
```

# Działanie aplikacji:

## Dodanie nowego zadania bez ustalenia opcji "completed":
![](3)

## Dodanie nowego zadania z opcją "completed":
![](4)

## Gotowe zadanie pojawiło się pod zakładką "complete"
![](5)

## Zadanie do zrobienia pojawiło się pod zakładką "incomplete"
![](6)

## ToDo listy pojawiają się również w naszym "API":
![](7)

## Po kliknięciu Delete usuń można usunąc wybrany ToDo:

## Przed usunięciem:
![](8)

## Po usunięciu:
![](9)



