import getpass
import os
import sys

import sublime
import sublime_plugin

MAX_SIZE = 10

class CopyToolCommand(sublime_plugin.TextCommand):
    copyed_queue = []

    def run(self, edit, origin_command=None, to_show=None):
        file_name = self.view.file_name() or "empyt_file_name"
        file_name = os.path.basename(file_name)
        if origin_command:
            self.view.run_command(origin_command)
        if to_show:
            self.show()
        else:
            copy_value = sublime.get_clipboard()
            self.put({
                "value": copy_value,
                "file_name": file_name,
            })
            print(CopyToolCommand.copyed_queue)

    def put(self, value):
        if len(CopyToolCommand.copyed_queue) == MAX_SIZE:
            CopyToolCommand.copyed_queue = CopyToolCommand.copyed_queue[1:]
        CopyToolCommand.copyed_queue.append(value)

    def get_all(self):
        return ["{}: {} -- {}".format(idx + 1, v["file_name"], v["value"].lstrip()[:80]) for idx, v in enumerate(reversed(CopyToolCommand.copyed_queue))]

    def select_idx(self, idx):
        if idx == -1:
            return
        content = CopyToolCommand.copyed_queue[len(CopyToolCommand.copyed_queue) - idx - 1]["value"]
        sublime.set_clipboard(content)
        self.view.run_command("paste_and_indent", {"characters": content})

    def show(self):
        self.view.window().show_quick_panel(
          self.get_all(),
          lambda x: self.select_idx(x),
        )
