#!/bin/bash
container_name=(homepage_server homepage_db homepage_restore)
server_address=95.163.202.160
project_name="homepage-server"

function deploy() {
  stopRemote

  echo "===================================>"
  #  rsync的desc会自动创建一个目录，所以这样就是/root/${project_name}
  echo "deploy....."
  echo "maybe a little bit slow because will push this file to your-server"
  rsync -avz --delete ../${project_name} root@${server_address}:/root

  cmd="cd ${project_name}/docker;"
  for data in ${container_name[@]}
  do
      cmd=${cmd}"docker-compose up --build -d ${data};"
  done
  echo ${cmd}
  ssh root@${server_address} ${cmd}
}

function getRemote() {
  echo "getting....."
  rsync -avz --delete root@${server_address}:/root/${project_name} ../
}

function stopRemote() {
  echo "stop....."
  cmd=""
  for data in ${container_name[@]}
  do
      cmd=${cmd}"docker rm -f ${data} || true;"
  done
  echo ${cmd}
  ssh root@${server_address} ${cmd}
}

function logRemote() {
  echo "docker logs -f ${container_name[0]}......"
  ssh root@${server_address} "docker logs -f ${container_name[0]}"
}

#get remote database sql to local
function dump() {
  mysqldump -h${DB_HOST} -u$root -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} > ./db/sql/latest_dump.sql
}

function restore() {
  second=10
  echo "sleep ${second} seconds to wait db start"
  sleep ${second}
  echo "mysql -h${DB_HOST} -uroot -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./db/sql/latest_dump.sql"
  mysql -h${DB_HOST} -uroot -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < ./db/sql/latest_dump.sql
}

function updateServer() {
  rsync -avz ../${project_name} root@${server_address}:/root
  echo "-------------------------------->"
  echo "update remove server....."
  cmd="cd ${project_name}/docker;"
  cmd=${cmd}"docker rm -f ${container_name[0]};"
  cmd=${cmd}"docker-compose up --build -d ${container_name[0]};"
  echo ${cmd}
  ssh root@${server_address} ${cmd}
}

case "$1" in
  deploy)
    deploy
    ;;

  stopRemote)
    stopRemote
    ;;

  getRemote)
    getRemote
    ;;

  logRemote)
    logRemote
    ;;

  dump)
    dump
    ;;

  restore)
    restore
    ;;

  updateServer)
    updateServer
    ;;
  *)
    echo "please choose one {dump | restore}"
    exit 1
esac
