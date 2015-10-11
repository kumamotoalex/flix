import React, { Component } from 'react';
import Card from 'material-ui/lib/card/card';
import CardMedia from 'material-ui/lib/card/card-media';
import CardActions from 'material-ui/lib/card/card-actions';
import Toolbar from 'material-ui/lib/toolbar/toolbar';
import ToolbarGroup from 'material-ui/lib/toolbar/toolbar-group';
import RaisedButton from 'material-ui/lib/raised-button';
import FlatButton from 'material-ui/lib/flat-button';
import TextField from 'material-ui/lib/text-field';
import FloatingButton from 'material-ui/lib/floating-action-button';
import IconButton from 'material-ui/lib/icon-button';

export default class SuggestionBar extends Component {
  constructor(props) {
    super(props);
    this.state = {notRated:[]};
  }
  render() {
    return (
      <div className="row">
          <div className="col m2 offset-m12">
              <IconButton iconClassName="material-icons" tooltipPosition="bottom-center" tooltip="Reset preferences">autorenew</IconButton>
          </div>
        <div className="row">
          <MovieList update={this.getNotRated} notRated={this.state.notRated}/>
        </div>
      </div>
    );
  }

  componentWillMount() {
    this.getNotRated();
  }

  getNotRated = () => {
    var self = this;
    var url = 'http://localhost:5000/getnotrated/' + 'obama';
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
class MovieList extends Component {
  render() {
    var Movies = this.props.notRated.slice(0,4).map(function(movie, i){
      return (
        <MovieCard update = {this.props.update} title={movie['title']} url = {movie['url']} />
      )
    }.bind(this));
    return (
      <div className="row">
        {Movies}
      </div>
    );
  }
}
class MovieCard extends Component {
  render() {
    let buttonStyle = {
      fontSize: '150%',
      textAlign: 'center'
    };
    return (
      <div className="col m3">
        <Card>
          <CardMedia>
            <img src={this.props.url}/>
          </CardMedia>
          <CardActions>
            <div className="row">
              <FlatButton className="col m12" label="Like" labelStyle={buttonStyle} primary={true} onClick={this.likeMovie}/>
              <FlatButton className="col m12" label="Dislike" labelStyle={buttonStyle} secondary={true} onClick={this.dislikeMovie}/>
            </div>
          </CardActions>
        </Card>
      </div>
    );
  }

  likeMovie = () => {
      var data = {
      'username': 'obama',
      'movie_likes': [this.props.title],
      'movie_dislikes': []
      };

      data = JSON.stringify(data);
    $.ajax({
      url: 'http://localhost:5000/sendscore',
      contentType: 'application/json',
      dataType:'json',
      type: 'POST',
      data: data,
      processData: false,
      success: (data) => {
        this.props.update()
      },
      error: function(data) {
        console.error(data.statusText);
      }.bind(this)
    });
  }

  dislikeMovie = () => {
    var data = {
    'username': 'obama',
    'movie_likes': [],
    'movie_dislikes': [this.props.title]
    };

    data = JSON.stringify(data);
    $.ajax({
      url: 'http://localhost:5000/sendscore',
      contentType: 'application/json',
      dataType:'json',
      type: 'POST',
      data: data,
      processData: false,
      success: function(data) {
        this.props.update();
      }.bind(this),
      error: function(data) {
        console.error(data.statusText);
      }.bind(this)
    });
  }
}
