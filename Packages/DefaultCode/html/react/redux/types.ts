/* eslint-disable import/prefer-default-export */
import { Action } from 'redux';

import Shift from 'models/shiftScheduler/Shift';

export interface SchedulerState {
  shiftList: Shift[];
  isPublished: boolean;
}

export enum SchedulerActionType {
  FETCH_SHIFT_LIST_COMPLETE = 'SCHEDULER.FETCH_SHIFT_LIST_COMPLETE',
}

interface FetchShiftListCompleteAction
  extends Action<SchedulerActionType.FETCH_SHIFT_LIST_COMPLETE> {
  shiftList: Shift[];
  isPublished: boolean;
}

export type SchedulerAction = FetchShiftListCompleteAction;
