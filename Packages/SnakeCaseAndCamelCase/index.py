import getpass
import os
import sys

import sublime
import sublime_plugin

sys.path.append('/home/{}/.local/lib/python3.5/site-packages'.format(getpass.getuser()))
sys.path.append('/home/{}/.local/lib/python3.8/site-packages'.format(getpass.getuser()))
sys.path.append('/usr/local/lib/python3.9/site-packages')

try:
    import humps
except Exception as e:
    sublime.message_dialog(str(e) + '\npip3 install pyhumps')
    # pass
class SnakeCaseAndCamelCaseCommand(sublime_plugin.TextCommand):
    str_to_convert = ""

    def run(self, edit):
        file_name = self.view.file_name() or "empyt_file_name"
        file_name = os.path.basename(file_name)
        region = self.view.sel()[0]
        if region.empty():
            self.view.show_popup('empty')
            return
        self.str_to_convert = self.view.substr(region)
        result = self.to_snake()
        result.extend(self.to_camel())
        def on_select(x):
            if x == -1:
                return
            self.view.run_command("snake_case_and_camel_case_cb", {"text": result[x]})

        self.view.window().show_quick_panel(
          result,
          on_select,
        )
        print(result)
    
    def to_snake(self):
        # intput:
        #   abCdEf || AbCdEf
        # output:
        #   ab_cd_ef
        #   AB_CD_EF
        tmp = self.str_to_convert
        return [
            humps.decamelize(tmp),
            humps.decamelize(tmp).upper(),
        ]

    def to_camel(self):
        # input:
        #   ab_cd_ef || AB_CD_EF
        # output:
        #   abCdEf
        #   AbCdEf
        tmp = self.str_to_convert.lower()
        return [
            humps.camelize(tmp),
            humps.pascalize(tmp),
        ]


class SnakeCaseAndCamelCaseCbCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        region = self.view.sel()[0]
        # print(text)
        self.view.replace(edit, region, text)
