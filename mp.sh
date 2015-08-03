#!/bin/bash

killbyname () {
  #echo "$1"
  $(ps aux | grep "$1" | grep -v grep | awk '{print "kill " $2}' | sh)
}

killbyname "sh /home/imegumii/Scripts/mplayerthing.sh"
ssh -p 777 -N -L6600:127.0.0.1:6600 imegumii@www.imegumii.nl & sh ~/Scripts/mplayerthing.sh & ncmpcpp ; killall mplayer & killbyname "sh /home/imegumii/Scripts/mplayerthing.sh" & killbyname "ssh -p 777 -N -L6600"

