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
		else:
			self.error_code(edit)		

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

    </body>
</html>
'''
		self.view.insert(edit, 0, code)

	def py_code(self, edit):
		self.view.insert(edit, 0, "vimi")

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
		self.view.insert(edit, 0, "vimi")

	def js_code(self, edit):
		code = """function count(start, end) {
    console.log(start);
    total = start + 1;
    e = end;
    vimi = setInterval(function show() {
        console.log(total);
        total++;
        if (total == e + 1) {
            clearInterval(vimi)
        }
    }, 100);

    return {
        cancel: function() {
            clearInterval(vimi);
        }
    }
}"""
		self.view.insert(edit, 0, code)

	def error_code(self, edit):
		self.view.insert(edit, 0, "error_code")
