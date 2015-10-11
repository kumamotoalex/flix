import React, { Component } from 'react';
import SuggestionBar from './SuggestionBar.js';
import UserTable from './UserTable.js';

export default class Body extends Component {
  render() {
    return (
      <div className="container">
        <SuggestionBar name={this.props.name}/>
        <UserTable name={this.props.name}/>
      </div>
    );
  }
}


