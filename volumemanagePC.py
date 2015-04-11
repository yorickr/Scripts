#!/bin/python

import alsaaudio
import sys
from gi.repository import Notify

#http://pyalsaaudio.sourceforge.net/libalsaaudio.html

# Making 3 mixer object because no feasible workaround :/
print(alsaaudio.mixers())
m1 = alsaaudio.Mixer('Master')
m2 = alsaaudio.Mixer('Front')
m3 = alsaaudio.Mixer('Headphone')
m4 = alsaaudio.Mixer('Surround')
m5 = alsaaudio.Mixer('Center')
m6 = alsaaudio.Mixer('Side')
m7 = alsaaudio.Mixer('Line')
m8 = alsaaudio.Mixer('LFE')

# Volume up by 5%
def volumeup():
    vol = m1.getvolume()
    newvol = vol[0] + 5
    try:
        m1.setvolume(newvol)
        sendNotification("Volume up")
    except alsaaudio.ALSAAudioError:
        sendNotification("Volume can't go over 100")
    
# Volume down by 5%
def volumedown():
    vol = m1.getvolume()
    newvol = vol[0] - 5
    try:
        m1.setvolume(newvol)
        sendNotification("Volume down")
    except alsaaudio.ALSAAudioError:
        sendNotification("Volume can't go below 0")

# Mute toggle
def mute():
    mute = m1.getmute()
    if mute[0] == 0:
        m1.setmute(1)
        m2.setmute(1)
        m3.setmute(1)
        m4.setmute(1)
        m5.setmute(1)
        m6.setmute(1)
        m7.setmute(1)
        m8.setmute(1)
        sendNotification("Mute")
    else:
        m1.setmute(0)
        m2.setmute(0)
        m3.setmute(0)
        m4.setmute(0)
        m5.setmute(0)
        m6.setmute(0)
        m7.setmute(0)
        m8.setmute(0)
        sendNotification("Unmute")

def sendNotification(string):
    Notify.init("Audio Notification")
    notification = Notify.Notification.new(string)
    notification.show()

try:
    if sys.argv[1] in "up":
        volumeup()
    elif sys.argv[1] in "down":
        volumedown()
    elif sys.argv[1] in "mute":
        mute()
    else:
        print("Not a valid argument, use \"up\", \"down\" or \"mute\"")
except IndexError:
    print("Insufficient arguments.")
