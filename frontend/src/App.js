import React, { Component } from 'react';
import Navbar from './Navbar.js';
import Body from './Body.js';

export default class App extends Component {
  render() {
    return (
      <div>
      <Navbar />
      <Body />
      </div>
    );
  }
}