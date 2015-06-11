#!/bin/bash
runplayer=true
while $runplayer
do nohup mplayer "http://localhost:9999/mpd.mp3" > /dev/null
  sleep 3
done 
