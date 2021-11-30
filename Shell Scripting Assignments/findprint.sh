#!/bin/bash


echo "Here are the lines that have printf in $1"

grep -w printf $1

echo "The number of lines that have printf in them is"
grep -c "printf" $1
