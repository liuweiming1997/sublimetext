import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import Divider from '@material-ui/core/Divider';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import Typography from '@material-ui/core/Typography';
import { withStyles, StyleRulesCallback, Theme, WithStyles } from '@material-ui/core/styles';
import { throttle } from 'lodash';

import Operator from 'models/operatorManagement/Operator';
import operatorApi from 'common/api/operatorApi';
import OperatorSearchForm from 'common/component/UserPicker/type';
import { Region } from 'common/proto/js_out/framework/region_pb';
import { ValueOf } from 'common/utils/types';

const styles: StyleRulesCallback<Theme, {}> = () => ({
  root: {
    height: 720,
    width: 600,
    backgroundColor: '#FFFFFF',
    boxShadow: '0 4px 10px 0 rgba(147,149,153,0.6)',
  },
});

interface Props extends WithStyles<typeof styles> {
  onClose: () => void;
  onConfirm: () => void;
  region: ValueOf<Region.RegionNameMap>;
}

class AddTagDialog extends React.PureComponent<Props> {
  private static SEARCH_DELAY = 500; // ms

  public componentDidMount(): void {
    this.getVehicleUsageWithFilterSet();
  }

  private getVehicleUsageWithFilterSet = throttle(async () => {
    const searchForm = new OperatorSearchForm();
    searchForm.region = region;
    const response = await operatorApi.getCandidateOperators(searchForm);
    if (!response) {
      return;
    }
  }, AddTagDialog.SEARCH_DELAY);

  public render(): React.ReactElement {
    const { classes, onClose, onConfirm } = this.props;
    return (
      <Dialog open classes={{ paper: classes.root }} maxWidth="md" onClose={onClose}>
        <MuiDialogTitle disableTypography>
          <Typography variant="h6">Tag Information</Typography>
        </MuiDialogTitle>
        <Divider />
        <DialogContent />
        <DialogActions>
          <Button onClick={onClose} variant="outlined">
            Cancel
          </Button>
          <Button onClick={() => onConfirm()} variant="contained" color="primary">
            Confirm
          </Button>
        </DialogActions>
      </Dialog>
    );
  }
}

export default withStyles(styles)(AddTagDialog);
