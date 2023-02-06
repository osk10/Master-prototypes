import subprocess

print("Running core")


def run_tool(path):
    p = subprocess.Popen(["python", path, "hahahah"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.stdin.write(bytes("sggindsgiundgsisg" + "\n", "ascii"))
    p.stdin.flush()
    out, error = p.communicate()
    print(out.decode("ascii"))


run_tool("/Users/oskar/Documents/Skole/Master/Prototypes/Run function in subprocess/tool/tool.py")
