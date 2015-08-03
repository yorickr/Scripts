#!/bin/bash

if [ "$1" = "s" ]; then
  pax11publish -e -S 192.168.1.133
else
  pax11publish -e -r
fi
