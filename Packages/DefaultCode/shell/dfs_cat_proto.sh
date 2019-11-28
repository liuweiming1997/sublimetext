#!/bin/bash
readonly PROTO_FILES=(
  "vehicle_scheduler/trip_info.proto"
)

readonly PREFIX_OF_IMPORT="import \"common/interface/"

function separate_import() {
  # echo "`cat vehicle_scheduler/trip_info.proto`"
  dependency_proto_file=(`grep -i "${PREFIX_OF_IMPORT}" vehicle_scheduler/trip_info.proto | awk -F'"' '{print substr($2, 18)}'`)
  file_length=${#dependency_proto_file[@]}
  if [[ $file_length -eq 0 ]]; then
    echo $x
  else
    for x in ${dependency_proto_file[@]}
    do
      echo $x
      separate_import $x
    done
  if
}

separate_import $1
# cat ${1}
