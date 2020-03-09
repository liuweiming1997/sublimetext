import { Reducer } from 'redux';

import { SchedulerState, SchedulerActionType, SchedulerAction } from './types';

const initialState: SchedulerState = {
  shiftList: [],
  isPublished: false,
};

export const schedulerReducer: Reducer<SchedulerState, SchedulerAction> = (
  state = initialState,
  action,
) => {
  switch (action.type) {
    case SchedulerActionType.FETCH_SHIFT_LIST_COMPLETE:
      return {
        ...state,
        shiftList: action.shiftList,
        isPublished: action.isPublished,
      };
    default:
      return state;
  }
};

export default { schedulerReducer };
