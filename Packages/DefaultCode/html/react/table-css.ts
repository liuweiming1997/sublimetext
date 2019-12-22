import { StyleRulesCallback, Theme } from '@material-ui/core/styles';

const TableStyles: StyleRulesCallback<Theme, {}> = theme => ({
  fatherDiv: {
    margin: 'auto',
    position: 'relative',
    flexGrow: 1,
    width: '100%',
    height: '100%',
  },
  dataTable: {
    width: '100%',
    height: '100%',
    overflow: 'auto',
    position: 'absolute',
  },
  paginationFooterSpacer: {
    flex: '0 1 0', // align the page controls on the left
  },
  fixedTableHead: {
    backgroundColor: '#fff',
    position: 'sticky',
    top: 0,
    marginLeft: theme.spacing(),
    marginRight: theme.spacing(),
    fontWeight: 'bold',
  },
  fixedTableFoot: {
    backgroundColor: '#fff',
    position: 'sticky',
    bottom: 0,
    marginLeft: theme.spacing(),
    marginRight: theme.spacing(),
  },
  tableCellPadding: {
    padding: 12,
  },
});

export default TableStyles;
