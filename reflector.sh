#!/bin/bash
reflector --verbose -l 20 --sort rate --save /etc/pacman.d/mirrorlist
