#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 根据文档确定的返回消息
class resp(object):
    def __init__(self, success, error, data):
        self.success = success  # bollean
        self.error = error      # string
        self.data = data        # interface

def work():
    resp_obj = resp(True, False, [1, 2, 3, 4, "a list"])
    return json.dumps(resp_obj, default = lambda obj: obj.__dict__, sort_keys=True, indent=4)

if __name__ == '__main__':
    json_value = work()
    print(json_value)
