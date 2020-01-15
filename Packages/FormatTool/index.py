import getpass
import os
import sys

import sublime
import sublime_plugin

from .util import py_yapf

class FormatToolCommand(sublime_plugin.TextCommand):
  def run(self, edit):
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

    region = self.view.sel()[0]
    if region.empty():
        self.view.show_popup('will using the whole file')
        return
    tot_str = self.view.substr(region)
    
    if suffix == 'py':
        result = py_yapf(1, 10, '/home/vimi/aaaavimidatafile/test/python/main.py')
    else:
        self.view.show_popup('Unsupport format file type')
