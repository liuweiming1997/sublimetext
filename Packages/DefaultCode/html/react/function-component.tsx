import React from 'react';
import { withStyles, StyleRulesCallback, Theme, WithStyles } from '@material-ui/core/styles';

const styles: StyleRulesCallback<Theme, {}> = () => ({
  root: {},
});

interface Props extends WithStyles<typeof styles> {}

const Warpper: React.FunctionComponent<Props> = ({
  classes,
}) => (
  <div>
    hello world
  </div>
);

export default withStyles(styles)(Warpper);

