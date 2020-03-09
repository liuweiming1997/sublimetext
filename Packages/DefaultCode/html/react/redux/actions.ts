/* eslint-disable import/prefer-default-export */
import { ActionCreator } from 'redux';
import { ThunkAction } from 'redux-thunk';

import { SchedulerActionType, SchedulerAction } from './types';

import { Region, Office } from 'common/proto/js_out/framework/region_pb';
import { TripType } from 'common/proto/js_out/vehicle_scheduler/enums_pb';
import { ValueOf } from 'common/utils/types';
import Shift from 'models/shiftScheduler/Shift';
import shiftApi from 'common/api/shiftApi';

type SchedulerThunkAction = ThunkAction<Promise<void>, {}, void, SchedulerAction>;
type SchedulerActionCreator = ActionCreator<SchedulerAction>;

// Fetch ShiftList
export const fetchShiftList = (
  dateStr: string,
  region: ValueOf<Region.RegionNameMap>,
  office: ValueOf<Office.EnumMap>,
  filterVehicleId?: number,
  filterDriverId?: number,
  filterCoDriverId?: number,
  filterFollowCarDriverId?: number,
  filterTypeOfUseage?: ValueOf<TripType.EnumMap>,
): SchedulerThunkAction => async dispatch => {
  const response = await shiftApi.getShifts(
    dateStr,
    region,
    office,
    filterVehicleId,
    filterDriverId,
    filterFollowCarDriverId,
    filterTypeOfUseage,
  );
  if (!response) {
    dispatch({
      type: SchedulerActionType.FETCH_SHIFT_LIST_COMPLETE,
      shiftList: [],
      isPublished: false,
    });
    return;
  }
  const isPublished = response.getIsPublished() || false;
  const shiftList = response.getShiftList().map(v => new Shift(v));
  dispatch({
    type: SchedulerActionType.FETCH_SHIFT_LIST_COMPLETE,
    shiftList,
    isPublished,
  });
};
