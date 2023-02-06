import datetime

def write_date():
    f = open("text-file.txt", "a")
    f.write("Time: " + str(datetime.datetime.now()) + "\n")
    f.close()

def write_string(text):
    f = open("text-file.txt", "a")
    f.write(text + "\n")
    f.close()
