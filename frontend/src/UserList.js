import React, { Component } from 'react';
import Avatar from 'material-ui/lib/avatar';
import Table from 'material-ui/lib/table/table';
import TableHeader from 'material-ui/lib/table/table-header';
import TableRow from 'material-ui/lib/table/table-row';
import TableHeaderColumn from 'material-ui/lib/table/table-header-column';
import TableRowColumn from 'material-ui/lib/table/table-row-column';
import TableBody from 'material-ui/lib/table/table-body';
import RaisedButton from 'material-ui/lib/raised-button';
import MapDialog from './MapDialog.js';
let standardActions = [
  { text: 'Cancel' },
  { text: 'Submit' }
];

export default class UserList extends Component {
  render() {
    return(
      <Table selectable={false}>
        <TableHeader adjustForCheckbox={false} displaySelectAll={false}>
          <TableHeaderColumn colSpan="3" style={{textAlign: 'center'}}>
          People to chill with
          </TableHeaderColumn>
        </TableHeader>
        <TableBody displayRowCheckbox={false}>
          <User />
        </TableBody>
      </Table>
    );
  }

  componentWillMount() {
    //GET list of matched users
  }
}

class User extends Component {
  render() {
    return (
        <TableRow >
          <TableRowColumn colSpan="4">
            <Avatar src = "../img/profile1.jpg" />
            John Smith
          </TableRowColumn>
          <TableRowColumn>
            <MapDialog />
          </TableRowColumn>
        </TableRow>
    );
  }
}
