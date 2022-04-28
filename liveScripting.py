# liveScripting.py
from microbit import *

sleep(1000)

s = ""
t = ""

while True:
    s = input("> ")
    if(s != 'run'):
        t = t + s + "\n"
    else:
        exec(t)
        t = ""
