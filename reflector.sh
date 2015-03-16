#!/bin/bash
reflector --verbose -l 200 --sort rate --save /etc/pacman.d/mirrorlist
