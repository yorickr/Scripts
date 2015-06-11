#!/bin/bash

ssh -p 777 -N -L9999:127.0.0.1:9999 imegumii@www.imegumii.nl & ssh -p 777 -N -L6600:127.0.0.1:6600 imegumii@www.imegumii.nl & sh ~/Scripts/mplayerthing.sh & ncmpcpp ; $(ps aux | grep "sh /home" | grep -v grep | awk '{print "killall mplayer && killall ssh && kill " $2}' | sh)

