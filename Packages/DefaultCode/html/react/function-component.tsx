import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
}));

interface Props {}

const Warpper: React.FunctionComponent<Props> = ({}) => {
  const classes = useStyles({});
  return (
    <div>
      hello world
    </div>
  )
};

export default Warpper;
