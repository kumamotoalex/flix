import React, { Component } from 'react';
import SuggestionBar from './SuggestionBar.js';
import UserList from './UserList.js';

export default class Body extends Component {
  render() {
    return (
      <div className="container">
        <SuggestionBar />
        <UserList />
      </div>
    );
  }
}


