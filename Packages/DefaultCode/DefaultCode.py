import getpass
import os
import sys

import sublime
import sublime_plugin

def read_file(floder_name, file_name):
  username = getpass.getuser()
  try:
    return open('/home/{}/.config/sublime-text-3/Packages/DefaultCode/{}/{}'.format(username, floder_name, file_name), 'r')
  except Exception as e:
    print(e)
    sublime.error_message('no such file {}/{}'.format(floder_name, file_name))
    return None

def prepare_files(floder_name):
  username = getpass.getuser()
  path = '/home/{}/.config/sublime-text-3/Packages/DefaultCode/{}/'.format(username, floder_name)
  result = []
  for parent, dirnames, filenames in os.walk(path, followlinks=True):
    for filename in filenames:
      result.append((os.path.join(parent, filename))[len(path):])
  return result

class DefaultCodeCommand(sublime_plugin.TextCommand):
  def write(self, fp, edit):
    content = fp.read() or 'having no content in {}'.format(fp.name)
    print(content)
    sublime.set_clipboard(content)
    self.view.run_command("paste_and_indent", {"characters": content})

  def showing(self, floder_name, edit):
    all_files = prepare_files(floder_name)
    self.view.window().show_quick_panel(
      all_files,
      lambda x: self.write(read_file(floder_name, all_files[x]) if x != -1 else None, edit)
    )

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
    elif suffix == "tsx" or suffix == "ts":
      self.tsx_code(edit)
    else: # 这个是makefile
      self.error_code(edit)

  def tsx_code(self, edit):
    self.showing('html', edit)

  def env_code(self, edit):
    self.showing('env', edit)

  def dockerfile_code(self, edit):
    self.showing('docker', edit)

  def proto_code(self, edit):
    self.showing('proto', edit)

  def header_file_code(self, edit):
    self.showing('cpp', edit)

  def yaml_code(self, edit):
    self.showing('docker', edit)

  def shell_code(self, edit):
    self.showing('shell', edit)

  def html_code(self, edit):
    self.showing('html', edit)

  def py_code(self, edit):
    self.showing('py', edit)

  def cpp_code(self, edit):
    self.showing('cpp', edit)

  def go_code(self, edit):
    self.showing('go', edit)

  def js_code(self, edit):
    self.showing('html', edit)

  def error_code(self, edit):
    self.showing('makefile', edit)
