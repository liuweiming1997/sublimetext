import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import Divider from '@material-ui/core/Divider';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  root: {
    height: 720,
    width: 600,
    backgroundColor: '#FFFFFF',
    boxShadow: '0 4px 10px 0 rgba(147,149,153,0.6)',
  },
}));

interface Props {
  onClose: () => void;
  onConfirm: () => void;
}

const ClearShiftDialog: React.FunctionComponent<Props> = ({onClose, onConfirm }) => {
  const classes = useStyles({});
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
};

export default ClearShiftDialog;
