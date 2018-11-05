import sublime
import sublime_plugin


class DefaultCodeCommand(sublime_plugin.TextCommand):
	def run(self, edit, args):
		name = self.view.file_name()
		suffix = ""
		index = name.rfind(".")

		if index == -1:
			suffix = "error_suffix"
		else:
			index += 1
			while index < len(name):
				suffix += name[index]
				index += 1


		if suffix == "py":
			self.py_code(edit)
		elif suffix == "cpp":
			self.cpp_code(edit)
		elif suffix == "js":
			self.js_code(edit)
		elif suffix == "go":
			self.go_code(edit)
		elif suffix == "html":
			self.html_code(edit)
		elif suffix == "sh":
			self.shell_code(edit)
		elif suffix == "yaml" or suffix == "yml":
			self.yaml_code(edit)
		else: # 这个是makefile
			self.error_code(edit)		

	def yaml_code(self, edit):
		code = """version: '3'
services:
  main:
    build:
      context: ..
      dockerfile: docker/server.Dockerfile
    ports:
      - "8080:8080"
    restart: always

  nginx:
    image: nginx:latest
    # 端口映射
    ports:
        - "80:80"
    environment:
        - LANG=en_US.UTF-8
        - LANGUAGE=en_US:en
        - LC_ALL=en_US.UTF-8
    # 数据卷
    volumes:
        # 映射主机./conf.d目录到容器/etc/nginx/conf.d目录
        - "$PWD/nginx.conf:/etc/nginx/conf.d/default.conf"
        - "/root/show/:/show"
    restart: always"""
		self.view.insert(edit, 0, code)


	def shell_code(self, edit):
		code = """#!/bin/bash
container_name=(server db)
server_address=95.163.202.160
project_name="Frontend"

function deploy() {
	#  rsync的desc会自动创建一个目录，所以这样就是/root/${project_name}
	echo "maybe a little bit slow because will push this file to your-server"
	rsync -avz --delete ../${project_name} root@${server_address}:/root

	cmd="cd ${project_name}/docker;"
	for data in ${container_name[@]}
	do  
	    cmd=${cmd}"docker-compose up --build -d ${data};"
	done

	ssh root@${server_address} ${cmd}
}

function localtest() {
	echo "local debuging....."
	go run main.go
}


function getRemote() {
	echo "getting....."
	rsync -avz --delete root@${server_address}:/root/${project_name} ../
}

DBUSER=root
DBHOST=95.163.202.160
DBNAME=homework
DBPASSWORD=vimi

#get remote database sql to local
function dump() {
	mysqldump -h$DBHOST -u$DBUSER -p$DBPASSWORD $DBNAME > ./db/sql/latest_dump.sql
}

function restore() {
	mysql -h$DBHOST -u$DBUSER -p$DBPASSWORD $DBNAME < ./db/sql/latest_dump.sql
}

case "$1" in
	deploy)
		deploy
		;;

	localtest)
		localtest
		;;

	getRemote)
		getRemote
		;;

	dump)
		dump
		;;

	restore)
		restore
		;;

	*)
		echo "please choose one {dump | restore}"
		exit 1
esac"""
		self.view.insert(edit, 0, code)

	def html_code(self, edit):
		code = '''<!DOCTYPE html>
<html lang = "en">
    <head>
        <meta charset = "utf-8">
            <title>
                <!-- set title here -->
            </title>
        </meta>
    </head>

    <script src = "main.js"> 
        // 1、逻辑可以写在js，并且在js调用。
        // 2、也可以在这里写，然后调用。这里调用不了main.js的内容
    </script>

    <body>
    	<form action="http://127.0.0.1:8080" method="post">
  			<p>First name: <input type="text" name="fname" /></p>
		    <p>Last name: <input type="text" name="lname" /></p>
  			<input type="submit" value="Submit" />
		</form>
    </body>

    <body>
		<form id="test-form" action="http://127.0.0.1:8080" method="post" onsubmit="return checkForm()">
		    <p>First name: <input type="text" name="fname" /></p>
		    <p>Last name: <input type="text" name="lname" /></p>
  			<input type="submit" value="Submit" />
		</form>

		<script>
			function checkForm() {
			    var form = document.getElementById('test-form');
			    // 可以在此修改form的input...
			    // 继续下一步:
			    form.submit()
			    return true;
			}
		</script>
    </body>

</html>'''
		self.view.insert(edit, 0, code)

	def py_code(self, edit):
		code = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# 根据文档确定的返回消息
class resp(object):
	def __init__(self, success, error, data):
		self.success = success  # bollean
		self.error = error	    # string
		self.data = data        # interface

def work():
	resp_obj = resp(True, False, [1, 2, 3, 4, "a list"])
	return json.dumps(resp_obj, default = lambda obj: obj.__dict__, sort_keys=True, indent=4)

if __name__ == '__main__':
	json_value = work()
	print(json_value)'''
		self.view.insert(edit, 0, code)

	def cpp_code(self, edit):
		code = """#include <bits/stdc++.h>
using namespace std;

#define inf (0x3f3f3f3f)
typedef long long int LL;


int main() {
    freopen("data.txt", "r", stdin);

    return 0;
}
"""
		self.view.insert(edit, 0, code)

	def go_code(self, edit):
		code = """package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type vimi struct {
	Name string `json:"json_name"`
	ID   string `json:"json_id"`
}

func root(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()                                      //解析参数，默认是不会解析的
	w.Header().Add("Access-Control-Allow-Origin", "*") //设置跨域
	fmt.Println("get message from " + r.RemoteAddr)
	fmt.Println(r.Form)
	v := &vimi{`vimi`, `ming`}
	jsonValueOfV, _ := json.Marshal(v)
	fmt.Fprintf(w, string(jsonValueOfV)) //这个写入到w的是输出到客户端的
}

func main() {
	http.HandleFunc("/", root)               //设置访问的路由
	err := http.ListenAndServe(":8080", nil) //设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}"""
		self.view.insert(edit, 0, code)

	def js_code(self, edit):
		code = """'use strict'
var url = 'http://95.163.202.160:8080';

function success(text) {
    var textarea = document.getElementById('id_test');
    textarea.innerHTML = text;
}

function fail(code) {
    var textarea = document.getElementById('id_test');
    textarea.innerHTML = 'Error code: ' + code;
}

var request = new XMLHttpRequest(); // 新建Microsoft.XMLHTTP对象
request.onreadystatechange = function() { // 状态发生变化时，函数被回调
    if (request.readyState === 4) { // 成功完成
        // 判断响应结果:
        if (request.status === 200) {
            // 成功，通过responseText拿到响应的文本:
            return success(request.responseText);
        } else {
            // 失败，根据响应码判断失败原因:
            return fail(request.status);
        }
    } else {
        // HTTP请求还在继续...
    }
}
// 发送请求:
request.open('GET', url);
request.send();"""
		self.view.insert(edit, 0, code)

	def error_code(self, edit):
		code = """.PHONY: Frontend

deploy:
	@./shell/deploy.sh deploy

localtest:
	@./shell/deploy.sh localtest"""
		self.view.insert(edit, 0, code)
