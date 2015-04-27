#!/bin/bash
du -d 1 -h -c $1 | sort -h -r
