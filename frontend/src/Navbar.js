import React, { Component } from 'react';
export default class Navbar extends Component {
  render() {
      return (
      <nav>
        <div className="nav-wrapper">
          <a href="#" className="brand-logo center"><span style={{ fontFamily: 'Playfair Display', fontSize: '200%'}}>Flix</span></a>
          <ul id="nav-mobile" className="left hide-on-med-and-down">
          </ul>
        </div>
       </nav>
      );
    }
}
