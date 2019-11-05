import React from 'react';
import { withStyles, StyleRulesCallback, WithStyles, Theme } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import { throttle } from 'lodash';

import Paper from '@material-ui/core/Paper';
import TableWrapper from 'OperatorManagement/table';
import vehiclesApi from 'common/api/vehiclesApi';
import { withRegion } from 'common/RegionContext';

const styles: StyleRulesCallback<Theme, {}> = () => ({
  container: {
    height: '100%',
    flexGrow: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'space-between',
  },
  root: {
    flexGrow: 1,
    margin: 'auto',
    width: '100%',
    height: 'calc(100% - 0px)',
  },
  dataTable: {
    width: '100%',
    height: '100%',
    overflow: 'auto',
    position: 'absolute',
  },
});

interface Props extends WithStyles<typeof styles> {
  regionContext: { region: number };
}

class VehicleUsage extends React.PureComponent<Props> {
  private static SEARCH_DELAY = 500; // ms

  public componentDidMount(): void {
    this.getVehicleUsageWithFilterSet();
  }

  public componentDidUpdate(prevProps: Readonly<Props>): void {
    const {
      regionContext: { region },
    } = this.props;
    if (prevProps.regionContext.region === region) {
      return;
    }
    console.log('update');
  }

  private getVehicleUsageWithFilterSet = throttle(async () => {
    const response = await vehiclesApi.getVehicleUsage();
    console.log(response);
  }, VehicleUsage.SEARCH_DELAY);

  public render(): React.ReactElement {
    const { classes } = this.props;
    return (
      <div className={classes.container}>
        <Paper className={classes.root}>
          <Typography style={{margin: 'auto', position: 'relative', flexGrow: 1, height: 'calc(100% - 54px)', width: '100%'}}>
            <Typography component="div" className={classes.dataTable}>
              <TableWrapper
                displayRows={[]}
                onChangePage={() => {}}
                onChangeRowsPerPage={() => {}}
                originRows={[]}
                page={0}
                rowsPerPage={10}
                titles={(() => {
                  const idd = [];
                  for (let idx = 0; idx < 26; idx++) {
                    idd.push('weimingliu');
                  }
                  return idd;
                })()}
                totalCount={30}
              />
            </Typography>
          </Typography>
        </Paper>
      </div>
    );
  }
}

export default withRegion(withStyles(styles)(VehicleUsage));
