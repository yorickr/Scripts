#!/usr/bin/python

import sys
import os

print(sys.argv[1])

os.system("echo hi")

if sys.argv[1] == "3":
    print("switch to python 3")
    os.system("sudo unlink /usr/bin/python")
    os.system("sudo ln -s /usr/bin/python3.4 /usr/bin/python")
else :
    print("switch to python 2")
    os.system("sudo unlink /usr/bin/python")
    os.system("sudo ln -s /usr/bin/python2.7 /usr/bin/python")

