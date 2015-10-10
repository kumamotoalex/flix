import React, { Component } from 'react';

export default class Body extends Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col m6">
            <div className="card medium">
              <div className="card-image">
                <img src="http://www.wichitaorpheum.com/wp-content/uploads/2013/12/Forrest-Gump-Poster.jpg"> </img>
                <span className="card-title">Card Title</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

