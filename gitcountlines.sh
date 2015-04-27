#!/bin/bash
git ls-files | grep ."$1" | xargs wc -l
