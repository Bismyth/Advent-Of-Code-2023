#!/bin/bash
d=$(find Days/* -type d -name '[0-9]*' -printf "%f\n" | sort -V | tail -n 1)

newPath="Days/$((d + 1))"

mkdir $newPath
cp base.py $newPath/main.py
touch $newPath/input.txt
touch $newPath/sample.txt