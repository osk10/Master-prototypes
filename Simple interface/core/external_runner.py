import subprocess


def run_external_program(path):
    print("Main process running")
    s = subprocess.run(["python", path])
    print(s.returncode)


run_external_program("/Simple interface/tool/main.py")
