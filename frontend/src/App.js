import React, { Component } from 'react';
import Navbar from './Navbar.js';
import Body from './Body.js';

export default class App extends Component {
  render() {
    var split = document.URL.split('/')
    var name = split[split.length-1];
    return (
      <div className="red lighten-5">
      <Navbar name={name}/>
      <Body name={name}/>
      </div>
    );
  }
  componentWillMount() {
    var split = document.URL.split('/')
    var name = split[split.length-1];

    var url = "http://localhost:5000/makeuser/" + name;
    $.ajax({
      url: url,
      contentType: 'application/json',
      dataType:'json',
      type: 'GET',
      processData: false,
      success: function(data) {
        this.setState(data);
      }.bind(this),
      error: function(data) {
        console.error(data.statusText);
      }.bind(this)
    });


  }
}
