import subprocess

print("Main process running")

s = subprocess.run(["python", "/Users/oskar/Documents/Skole/Master/Prototypes/Simple subprocess/Subprocess/main.py"])


print(s.returncode)
