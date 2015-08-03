#!/usr/bin/env bash

icon="$HOME/.cache/icon.png"
tmpbg='/tmp/screen.png'

(( $# )) && { icon=$1; }

scrot "$tmpbg"
cp "$tmpbg" "$HOME/Screenshots//$(date +"%Y-%m-%d at %I.%M.%S").png"
convert "$tmpbg" -scale 10% -scale 1000% "$tmpbg"
convert "$tmpbg" "$icon" -gravity center -composite -matte "$tmpbg"
i3lock -d -I 5 -u -i "$tmpbg"
