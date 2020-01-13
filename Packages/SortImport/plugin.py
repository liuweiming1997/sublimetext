"""
    pony.hello hello
"""
import os
import datetime
import time
import sys
import abc
import copy
from sys import (
    path,
    api_version,
    call_tracing,
)

import sublime, sublime_plugin

from .lib.RegexUtil import RegexUtil

def cmp_func(key):
    return str(key).lower()

MAX_TRY_TIMES = 200

class SortImportCommand(sublime_plugin.TextCommand):
    def mulity_annotation(self, pattern):
        if len(pattern) >= 3 and pattern[0] == '"' and pattern[1] == '"' and pattern[2] == '"':
            return True
        return False
    
    def read_line(self, s):
        idx = 0
        while s[idx] != '\n':
            idx += 1
        return s[:idx], idx

    def translate_str(self, tot_str) -> '[[], [], []], str':
        if tot_str[-1] != '\n':
            tot_str += '\n'
        result, sub_result, start_idx, try_time, still_continue, header = [], [], 0, 0, False, ''
        while True:
            try_time += 1
            if try_time == MAX_TRY_TIMES:
                return None
            if start_idx >= len(tot_str):
                break
            one_line, add = self.read_line(tot_str[start_idx:])
            start_idx += add + 1

            if self.mulity_annotation(one_line):
                header += one_line + '\n'
                still_continue = not still_continue
                continue
            if still_continue:
                header += one_line + '\n'
                continue

            if one_line == '':
                result.append(sub_result)
                sub_result = []
            elif one_line[-1] == '(':
                sort_inside = []
                while True:
                    temp_line, add = self.read_line(tot_str[start_idx:])
                    start_idx += add + 1
                    if temp_line[-1] == ')':
                        break
                    else:
                        sort_inside.append(temp_line)
                sort_inside.sort(key=cmp_func)
                one_line += '\n'
                for value in sort_inside:
                    one_line += value + '\n'
                one_line += ')'
                sub_result.append(one_line)
            else:
                sub_result.append(one_line)

        if len(sub_result) > 0:
            result.append(sub_result)
        return result, header

    def version_two(self, edit):
        region = self.view.sel()[0]
        if region.empty():
            self.view.show_popup('empty')
            return
        tot_str = self.view.substr(region)
        arr_str, header = self.translate_str(tot_str)
        if arr_str is None:
            self.view.show_popup('fuck, many time')
            return
        ans = header
        for value in arr_str:
            value.sort(key=cmp_func)
            for k in value:
                ans += k + '\n'
            ans += '\n'
        self.view.replace(edit, region, ans[:-2])

    def run(self, edit):
        # self.version_one()
        self.version_two(edit)
