import subprocess


def py_yapf(begin_line, end_line, file_path):
    cmd = ['yapf', '--style', '{based_on_style: google, column_limit:100}', '--lines', '{}-{}'.format(begin_line, end_line), file_path]
    return subprocess.check_output(cmd).decode('utf-8')


def goimports(begin_line, end_line, file_path):
    cmd = ["goimports", "-w", file_path]
    return subprocess.check_output(cmd).decode("utf-8")
