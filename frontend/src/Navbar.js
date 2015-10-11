import React, { Component } from 'react';
import Avatar from 'material-ui/lib/avatar';

export default class Navbar extends Component {
  render() {
    var split = document.URL.split('/');
    var name = split[split.length-1];
    var imgurl = "../img/" + name + ".jpg";

      return (
      <nav>
        <div className="nav-wrapper">
          <Avatar src = {imgurl}/>
          <span style={{fontSize:'150%'}}> {name}</span>
          <a href="#" className="brand-logo center"><span style={{ fontFamily: 'Playfair Display', fontSize: '200%'}}>Flix</span></a>
          <ul id="nav-mobile" className="left hide-on-med-and-down">
          </ul>
        </div>
       </nav>
      );
    }
}
