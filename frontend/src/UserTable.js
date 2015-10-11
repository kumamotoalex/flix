import React, { Component } from 'react';
import Avatar from 'material-ui/lib/avatar';
import Table from 'material-ui/lib/table/table';
import TableHeader from 'material-ui/lib/table/table-header';
import TableRow from 'material-ui/lib/table/table-row';
import TableHeaderColumn from 'material-ui/lib/table/table-header-column';
import TableRowColumn from 'material-ui/lib/table/table-row-column';
import TableBody from 'material-ui/lib/table/table-body';
import RaisedButton from 'material-ui/lib/raised-button';
import SnackBar from 'material-ui/lib/snackbar';

export default class UserTable extends Component {
  constructor(props) {
    super(props);
    this.state = {matches: []};
  }
  render() {
    var matches = this.state.matches.map((match) => {
      return (
        <User name={match[0]} score={match[1]} isChill={match[2]}  />
      );
    });

    return(
      <Table selectable={false}>
        <TableHeader adjustForCheckbox={false} displaySelectAll={false}>
          <TableHeaderColumn colSpan="3" style={{fontSize:'150%', textAlign: 'center'}}>
          People to chill with
          </TableHeaderColumn>
        </TableHeader>
        <TableBody displayRowCheckbox={false}>
          {matches}
        </TableBody>
      </Table>
    );
  }

  componentWillMount() {
    this.getUserList();
    //setInterval(this.getUserList, 500);
  }

  getUserList = () => {
    var url = 'http://localhost:5000/getmatches/' + this.props.name;
    $.ajax({
      url: url,
      contentType: 'application/json',
      dataType:'json',
      type: 'GET',
      processData: false,
      success: (data) => {
        this.setState(data);
      },
      error: function(data) {
        console.error(data.statusText);
      }.bind(this)
    });
  }
}

class User extends Component {
constructor(props) {
    super(props);
    this.toast = <SnackBar
                  message="Chill request sent!"
                  autoHideDuration={3000}
                  />
  }
  render() {
    var imgurl = "../img/" + this.props.name + ".jpg";
        return (
        <TableRow >
          <TableRowColumn colSpan="2"style={{fontSize:'150%', textAlign: 'left'}}>
            <Avatar src = {imgurl}/>
            {this.props.name}
          </TableRowColumn>
          <TableRowColumn colSpan="4"style={{fontSize:'150%', textAlign: 'left'}}>
          {this.props.isChill? "Wants to Chill" : "" }Chillscore: {this.props.score}
          </TableRowColumn>
          <TableRowColumn>
            <RaisedButton style={{fontSize:'150%', textAlign: 'right'}}label="Chill?" primary={true} onClick={this.sendChill}/>
          </TableRowColumn>
        </TableRow>
    );
  }

  sendChill = () => {
    var split = document.URL.split('/')
    var name = split[split.length-1];
    var url = 'http://localhost:5000/chill/' + name +'/' this.props.name;
    $.ajax({
      url:'http://localhost:5000/chill/',
      contentType: 'application/json',
      dataType:'json',
      type: 'GET',
      processData: false,
      success: (data) => {
        this.setState(data);
      },
      error: (data) => {
        console.error(data.statusText);
      }.bind(this)
    });
  }
}

