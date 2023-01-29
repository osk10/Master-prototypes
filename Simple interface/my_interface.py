from interface.core import write_date, write_string

print("External program running")
def add_time():
    write_date()

def add_text(text):
    write_string(text)

def add_text_time(text):
    write_date()
    write_string(text)