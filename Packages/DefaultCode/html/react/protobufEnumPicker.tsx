import React from 'react';
import { withStyles, StyleRulesCallback, Theme, WithStyles } from '@material-ui/core/styles';
import classNames from 'classnames';

import { SelectFilter } from 'common/component/filter';

const styles: StyleRulesCallback<Theme, {}> = () => ({
  picker: {
    display: 'block',
    overflow: 'visible',
  },
});

interface Option<T> {
  label: string;
  value: T[keyof T];
}

interface Props<T extends {}> extends WithStyles<typeof styles> {
  label: string;
  shrinkLabel?: string;
  className?: string;
  defaultValue?: T[keyof T];
  protobufEnum: T;
  onChange: (selected?: T[keyof T]) => void;
  renderer?: (name?: string, value?: number) => string;
}

function ProtobufEnumSinglePicker<T>({
  classes,
  label,
  shrinkLabel,
  className,
  onChange,
  defaultValue,
  protobufEnum,
  renderer,
}: Props<T>): React.ReactElement {
  const enumOptions: Option<T>[] = Object.entries(protobufEnum).map(([key, value]) => {
    return {
      value,
      label: (renderer && renderer(key, value)) || key,
    };
  });
  const found = enumOptions.find(v => v.value === defaultValue);
  const defaultValueOption = found && found;
  return (
    <React.Fragment>
      <SelectFilter
        options={enumOptions}
        className={classNames(className, classes.picker)}
        onChange={(selected?: Option<T>) => {
          onChange(selected ? selected.value : undefined);
        }}
        placeholder={label}
        value={defaultValueOption}
        textFieldProps={{
          label: shrinkLabel,
          InputLabelProps: {
            shrink: true,
          },
        }}
      />
    </React.Fragment>
  );
}

export default withStyles(styles)(ProtobufEnumSinglePicker) as <T>(
  props: Omit<Props<T>, 'classes'>,
) => JSX.Element;
