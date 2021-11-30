#! /bin/bash

cd $1

echo "directory has been changed to $1"
echo "here is the contents of that directory"
ls
echo "Here are all the lines that have 'print' in them:"

grep -w print *.tester

