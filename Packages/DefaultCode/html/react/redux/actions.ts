/* eslint-disable import/prefer-default-export */
import { ActionCreator } from 'redux';
import { ThunkAction } from 'redux-thunk';

import { VmsSearchActionType, VmsSearchAction } from './types';

import {
  VmsApiRequest as VmsApiRequestProto,
  SearchResponse as SearchResponseProto,
} from 'common/proto/js_out/vehicle_manager/api_pb';
import vehicleManagerApi from 'common/api/vehicleManagerApi';

type VmsSearchThunkAction = ThunkAction<Promise<void>, {}, void, VmsSearchAction>;
type VmsSearchActionCreator = ActionCreator<VmsSearchAction>;

export const doVmsSearch = (
  searchRequest: VmsApiRequestProto,
): VmsSearchThunkAction => async dispatch => {
  dispatch({ type: VmsSearchActionType.SEARCH_START });
  const vmsApiResponse = await vehicleManagerApi.doVmsSearch(searchRequest);
  if (!vmsApiResponse) {
    dispatch({
      type: VmsSearchActionType.SEARCH_COMPLETE,
      searchResponse: new SearchResponseProto(),
    });
    return;
  }
  dispatch({
    type: VmsSearchActionType.SEARCH_COMPLETE,
    searchResponse: vmsApiResponse.getSearchResponse() || new SearchResponseProto(),
  });
};
