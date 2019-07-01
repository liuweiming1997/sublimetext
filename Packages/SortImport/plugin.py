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
    line_number = 0

    def method_one(self):
        # not use this becase it will remove black line and will mistake variable
        should_sort_list = self.view.find_all('((?i))(.*)?((?i)import)(.*)?((?i))', 0)
        print(should_sort_list)
        for value in should_sort_list:
            ss = self.view.substr(sublime.Region(value.a, value.b))
            print(ss)

    def remove_trilling_space_and_line_change_key(self, origin_str):
        result = origin_str.rstrip()
        return result

    def get_line(self, fp):
        self.line_number += 1
        return fp.readline()

    def mulity_annotation(self, pattern):
        if len(pattern) >= 3 and pattern[0] == '"' and pattern[1] == '"' and pattern[2] == '"':
            return True
        return False

    def search_file(self, file_path_name, groups):
        var_for_kill = 0
        re = RegexUtil.get_regex(must_contain=['import', 'include'])
        should_end = RegexUtil.get_regex(must_contain='class ')
        with open(file_path_name, 'r') as fp:
            while var_for_kill < MAX_TRY_TIMES:
                var_for_kill += 1
                group = []
                always_continue = False
                while True:
                    one_line = self.get_line(fp)
                    one_line = self.remove_trilling_space_and_line_change_key(one_line)
                    if self.mulity_annotation(one_line):
                        if always_continue:
                            always_continue = False
                            continue
                        else:
                            always_continue = True
                    if always_continue:
                        continue
                    if len(one_line) == 0:
                        break
                    if one_line[0] == '#' or one_line[0] == '/':
                        continue
                    if should_end.match(one_line):
                        return
                    if re.match(one_line):
                        if one_line[-1] == '(':
                            one_line += '\n'
                            sort_inside = []
                            while True:
                                new_line = self.get_line(fp)
                                new_line = self.remove_trilling_space_and_line_change_key(new_line)
                                if new_line[-1] == ')':
                                    break
                                sort_inside.append(new_line)
                            sort_inside.sort(key=cmp_func)
                            for value in sort_inside:
                                one_line += value + '\n'
                            one_line += ')'
                        group.append(one_line)
                    else:
                        return
                if len(group) > 0:
                    groups.append(group)


    def version_one(self):
        self.line_number = 0
        file_path_name = self.view.file_name()
        groups = []
        self.search_file(file_path_name, groups)
        print(groups)
        print(self.line_number)


        update = False
        after_change = ''
        for value in groups:
            temp = copy.deepcopy(value)
            value.sort(key=cmp_func)
            for idx in range(0, len(value)):
                if (value[idx] != temp[idx]):
                    update = True

            for v in value:
                after_change += v
                after_change += '\n'
            after_change += '\n'
        after_change = after_change[:-2]
        print(after_change)

        if update:
            self.view.show_popup('!!!!!! update !!!!!!!!!')
        # buf = self.view.window().new_file()
        # buf.run_command('insert_commit_description', {'desc': after_change, 'scratch_view_name': 'sort import'})
        sublime.set_clipboard(after_change)
#################################################################################################################

    
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
