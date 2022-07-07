#make a function to write to a file
def write_to_file(filename, text):
    """
    Write text to a file
    """
    with open(filename, 'a') as f:
        f.write(text)
    return

def write_to_time(text):
    write_to_file("time.txt", text)

def overwrite(file,text):
    with open(file, "w") as f:
        f.write(text)
    return