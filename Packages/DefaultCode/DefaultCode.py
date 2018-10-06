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
		else:
			self.error_code(edit)		



	def py_code(self, edit):
		self.view.insert(edit, 0, "vimi")

	def cpp_code(self, edit):
		code = ""
		code += "#include <bits/stdc++.h>" + "\n"
		code += "using namespace std;" + "\n"
		code += "\n"
		code += "#define inf (0x3f3f3f3f)" + "\n"
		code += "typedef long long int LL;" + "\n"
		code += "\n\n"
		code += "int main() {" + "\n"
		code += "#ifdef local" + "\n"
		code += '    freopen("data.txt", "r", stdin);' + "\n"
		code += "#endif // local" + "\n"
		code += "\n"
		code += "    return 0;" + "\n"
		code += "}" + "\n"

		self.view.insert(edit, 0, code)

	def go_code(self, edit):
		self.view.insert(edit, 0, "vimi")

	def js_code(self, edit):
		self.view.insert(edit, 0, "vimi")

	def error_code(self, edit):
		self.view.insert(edit, 0, "error_code")
