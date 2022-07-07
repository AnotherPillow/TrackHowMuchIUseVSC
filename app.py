# import module
import psutil
from write import write_to_file as write
from write import overwrite
import time
  
# check if chrome is open

print("Code.exe" in (i.name() for i in psutil.process_iter()))

minutes = 0

#get current date
import datetime
now = datetime.datetime.now()
date = now.strftime("%d/%m/%y")
#read today.txt
with open("today.txt") as mytxt:
    for line in mytxt:
        if line.split(":")[0] == date:
            minutes = int(line.split(":")[1])
        else:
            yesterday = mytxt
            # if line includes "/"
            if "/" in line:
                write("time.txt", "{0}\n".format(line))
            
            overwrite("today.txt", "{0}:0".format(date))
while True:
    time.sleep(60)
    if "Code.exe" in (i.name() for i in psutil.process_iter()):
        print(minutes)
        minutes += 1
        overwrite("today.txt", "\n{0}:{1}".format(date, minutes))