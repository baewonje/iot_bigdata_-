import os
import glob
import time

f = os.popen("dir")
print(f.read())

print(glob.glob("*.py"))

print(time.strftime('%Y-%m-%d %p%I:%M:%S sec',time.localtime(time.time())))



