/* eslint-disable import/prefer-default-export */
import { Action } from 'redux';

import { SearchResponse as SearchResponseProto } from 'common/proto/js_out/vehicle_manager/api_pb';

export interface VmsSearchState {
  isSearching: boolean;
  searchResponse: SearchResponseProto;
}

export enum VmsSearchActionType {
  SEARCH_START = 'VMSSEARCH.SEARCH_START',
  SEARCH_COMPLETE = 'VMSSEARCH.SEARCH_COMPLETE',
}

interface SearchStartAction extends Action<VmsSearchActionType.SEARCH_START> {}

interface SearchCompleteAction extends Action<VmsSearchActionType.SEARCH_COMPLETE> {
  searchResponse: SearchResponseProto; 
}

export type VmsSearchAction =
  | SearchStartAction
  | SearchCompleteAction;
