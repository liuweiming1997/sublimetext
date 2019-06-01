import os
import datetime
import time
import sys
import abc

import sublime, sublime_plugin

from .lib.RegexUtil import RegexUtil


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

    def search_file(self, file_path_name, groups):
        var_for_kill = 0
        re = RegexUtil.get_regex(must_contain=['import', 'include'])
        should_end = RegexUtil.get_regex(must_contain='class')
        with open(file_path_name, 'r') as fp:
            while var_for_kill < MAX_TRY_TIMES:
                var_for_kill += 1
                group = []
                while True:
                    one_line = self.get_line(fp)
                    one_line = self.remove_trilling_space_and_line_change_key(one_line)
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
                            sort_inside.sort()
                            for value in sort_inside:
                                one_line += value + '\n'
                            one_line += ')'
                        group.append(one_line)
                    else:
                        return
                if len(group) > 0:
                    groups.append(group)


    def run(self, edit):
        self.line_number = 0
        file_path_name = self.view.file_name()
        groups = []
        self.search_file(file_path_name, groups)
        print(groups)
        print(self.line_number)

        after_change = ''
        for value in groups:
            value.sort()
            for v in value:
                after_change += v
                after_change += '\n'
            after_change += '\n'
        print(after_change)
        # with open(file_name, 'r') as fp:

        buf = self.view.window().new_file()
        buf.run_command('insert_commit_description', {'desc': after_change, 'scratch_view_name': 'sort import'})
        sublime.set_clipboard(after_change)
        # self.view.run_command("insert_snippet",
        #     {
        #         "contents": "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #     }
        # )
