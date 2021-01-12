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
    this.onChange = this.onChange.bind(this);

    this.state = {
      id: null,
      title: "",
      description: "", 
      published: false,
      upload: [],
      submitted: false,
      image: null,
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

  saveTutorial() {
      const formData = new FormData();
      console.log(this.state.upload)
      console.log(this.state.upload.name)
      formData.append("title", this.state.title);
      formData.append("description", this.state.description);
      formData.append("upload", this.state.upload, this.state.upload.name);

      axios.post("http://127.0.0.1:8080/api/tutorials", formData, {
        headers: {
          'content-type': 'multipart/form-data'
        } 
    });
      this.setState({
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
  onChange = e => {
    console.log(this.state.file)
    const files = Array.from(e.target.files)
    this.setState({
      upload: files[0],
      image: URL.createObjectURL(e.target.files[0])
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
              <Buttons onChange={this.onChange} />
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