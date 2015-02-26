# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 21:28:40 2015

@author: regof
"""

import time
import ctypes

count = 0

print "This break message was sent on "+time.ctime()
messageBox = ctypes.windll.user32.MessageBoxA
returnValue = messageBox(None, "Maybe it's time for you to stand up and have a break?", "News NRA Team Stand Up Program", 0x40 | 0x4)
if returnValue == 6:
    messageBox = ctypes.windll.user32.MessageBoxA
    returnValue = messageBox(None, "Great! I'll remind you again in 2 hrs to stand up and move!", "News NRA Team Stand Up Program", 0x40 | 0x0)
elif returnValue == 7:
    messageBox = ctypes.windll.user32.MessageBoxA
    returnValue = messageBox(None, "Are you sure? Stretch your back at least then... I'll be back in 2hrs!", "News NRA Team Stand Up Program", 0x40 | 0x0)

while (count < 4):
    time.sleep(60*60*2)
    print "This break message was sent on"+time.ctime()
    messageBox = ctypes.windll.user32.MessageBoxA
    returnValue = messageBox(None, "Maybe it's time for you to stand up and have a break?", "News NRA Team Stand Up Program", 0x40 | 0x4)
    if returnValue == 6:
        messageBox = ctypes.windll.user32.MessageBoxA
        returnValue = messageBox(None, "Great! I'll remind you again in 2 hrs to stand up and move!", "News NRA Team Stand Up Program", 0x40 | 0x0)
    elif returnValue == 7:
        messageBox = ctypes.windll.user32.MessageBoxA
        returnValue = messageBox(None, "Are you sure? Stretch your back at least then... I'll be back in 2hrs!", "News NRA Team Stand Up Program", 0x40 | 0x0)
    count = count + 1

time.localtime()
