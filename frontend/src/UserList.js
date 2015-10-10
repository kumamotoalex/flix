import React, { Component } from 'react';
import Avatar from 'material-ui/lib/avatar';
import Dialog from 'material-ui/lib/dialog';
import Table from 'material-ui/lib/table/table';
import TableHeader from 'material-ui/lib/table/table-header';
import TableRow from 'material-ui/lib/table/table-row';
import TableHeaderColumn from 'material-ui/lib/table/table-header-column';
import TableRowColumn from 'material-ui/lib/table/table-row-column';
import TableBody from 'material-ui/lib/table/table-body';

let standardActions = [
  { text: 'Cancel' },
  { text: 'Submit' }
];

export default class UserList extends Component {
  render() {
    return(
      <Table selectable={false}>
        <TableHeader adjustForCheckbox={false} displaySelectAll={false}>
          <TableHeaderColumn colSpan="3" tooltip='Super Header' style={{textAlign: 'center'}}>
          People to chill with
          </TableHeaderColumn>
        </TableHeader>
        <TableBody displayRowCheckbox={false}>
          <User />
        </TableBody>
      </Table>
      );
  }
}

class User extends Component {
  render() {
    return (
        <TableRow >
<TableRowColumn>
          <Avatar src = "../img/profile1.jpg" />
            John Smith</TableRowColumn>
            <TableRowColumn>Chill!</TableRowColumn>
        </TableRow>
    );
  }
}
