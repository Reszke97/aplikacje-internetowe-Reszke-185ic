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

function Home(){
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




class Lista extends Component {
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