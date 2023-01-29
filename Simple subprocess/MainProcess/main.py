import subprocess

print("Main process running")

s = subprocess.run(["python", "/Users/oskar/Documents/Skole/Master/Prototypes/Subprocess/Subprocess/main.py"])


print(s.returncode)
