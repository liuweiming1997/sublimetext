import { Reducer } from 'redux';

import { VmsSearchState, VmsSearchActionType, VmsSearchAction } from './types';

import { SearchResponse as SearchResponseProto } from 'common/proto/js_out/vehicle_manager/api_pb';

const initialState: VmsSearchState = {
  isSearching: false,
  searchResponse: new SearchResponseProto(),
};

export const vmsSearchReducer: Reducer<VmsSearchState, VmsSearchAction> = (
  state = initialState,
  action,
) => {
  switch (action.type) {
    case VmsSearchActionType.SEARCH_START:
      return {
        ...state,
        isSearching: true,
      };
    case VmsSearchActionType.SEARCH_COMPLETE:
      return {
        ...state,
        isSearching: false,
        searchResponse: action.searchResponse,
      };
    default:
      return state;
  }
};

export default { vmsSearchReducer };
