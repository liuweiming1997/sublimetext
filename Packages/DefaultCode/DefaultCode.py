import getpass
import os
import sys

import sublime
import sublime_plugin

def read_file(floder_name, file_name):
  username = getpass.getuser()
  return open('/home/{}/.config/sublime-text-3/Packages/DefaultCode/{}/{}'.format(username, floder_name, file_name), 'r')

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

    elif suffix == "cpp" or suffix == "cc":
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

    elif suffix == "h":
      self.header_file_code(edit)

    elif suffix == "proto":
      self.proto_code(edit)

    elif suffix == "dockerfile" or suffix == "Dockerfile":
      self.dockerfile_code(edit)

    elif suffix == "env":
      self.env_code(edit)
    elif suffix == "tsx":
      self.tsx_code(edit)
    else: # 这个是makefile
      self.error_code(edit)

  def tsx_code(self, edit):
    code = 'can not read'
    with read_file('html', 'pure-component.tsx') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def env_code(self, edit):
    code = 'can not read'
    with read_file('env', 'env.env') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def dockerfile_code(self, edit):
    code = 'can not read'
    with read_file('docker', 'server.dockerfile') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def proto_code(self, edit):
    code = 'can not read'
    with read_file('proto', 'official-demo.proto') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def header_file_code(self, edit):
    code = 'can not read'
    with read_file('cpp', 'header.h') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def yaml_code(self, edit):
    code = 'can not read'
    with read_file('docker', 'web-service.yaml') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def shell_code(self, edit):
    code = 'can not read'
    with read_file('shell', 'deploy.sh') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def html_code(self, edit):
    code = 'can not read'
    with read_file('html', 'html.html') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def py_code(self, edit):
    code = 'can not read'
    with read_file('py', 'default_class.py') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def cpp_code(self, edit):
    code = 'can not read'
    with read_file('cpp', 'acm.cpp') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def go_code(self, edit):
    code = 'can not read'
    with read_file('go', 'web-img-service.go') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def js_code(self, edit):
    code = 'can not read'
    with read_file('html', 'ajax.js') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)

  def error_code(self, edit):
    code = 'can not read'
    with read_file('makefile', 'Makefile') as fp:
      code = fp.read()
    self.view.insert(edit, 0, code)
