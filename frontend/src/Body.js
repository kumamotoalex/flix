import React, { Component } from 'react';
import SuggestionBar from './SuggestionBar.js';
import UserTable from './UserTable.js';

export default class Body extends Component {
  render() {
    return (
      <div className="container">
        <SuggestionBar />
        <UserTable />
      </div>
    );
  }
}


