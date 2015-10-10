import React, { Component } from 'react';
import Card from 'material-ui/lib/card/card';
import CardMedia from 'material-ui/lib/card/card-media';
import Toolbar from 'material-ui/lib/toolbar/toolbar'
import ToolbarGroup from 'material-ui/lib/toolbar/toolbar-group'
import RaisedButton from 'material-ui/lib/raised-button'

export default class SuggestionBar extends Component {
  render() {
    return (
      <div className="row">
        <AppBar />
        <MovieCard url="http://actuallyitdepends.files.wordpress.com/2012/01/forrestgump_mpw-19355.jpg"/>
        <MovieCard url="https://owlswellblog.files.wordpress.com/2013/11/frozen-a4.jpg" />
      </div>
    );
  }
}

class MovieCard extends Component {
  render() {
    return (
      <div className="col m3">
        <Card>
          <CardMedia>
            <img src={this.props.url}/>
          </CardMedia>
        </Card>
      </div>
    );
  }
}

class AppBar extends Component {
  render() {
    return(
      <Toolbar>
        <ToolbarGroup float="left">
          <RaisedButton label="CHILL" primary={true}/>
        </ToolbarGroup>
      </Toolbar>
    );
  }
}
