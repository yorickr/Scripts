#!/bin/bash

sh ~/Scripts/mplayerthing.sh & ncmpcpp ; $(ps aux | grep "sh /home" | grep -v grep | awk '{print "killall mplayer && kill " $2}' | sh)

