#!/bin/bash

echo "$1"

sudo chvt $1
startx /usr/bin/cinnamon-session
