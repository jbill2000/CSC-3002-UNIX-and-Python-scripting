#!/bin/bash

#asks user what core type they would like and records it
echo "Which core type (one-four) would you like to record?"

read coretype

#if coretype is = to one 
if [[ $coretype = "one" ]]
then
#prints some info
echo "Collecting data on type one"
echo "Here are the results: "
echo "Type one is the perfectionist or reformer"

#grep command to search for all files containing core type: one
#also outputs the data from the grep command into a file passed in with the
#positional parameter.

grep -l "core type: one" *.txt > $1 

#prints out the file

cat $1

#if user inputs two
elif [[ $coretype = "two" ]] 
then

#prints info
echo "Collecting data on type two"
echo "Here are the results: "
echo "Type two is the helper"

#grep command to search for all files containing core type: two               
#also outputs the data from the grep command into a file passed in with the   
#positional parameter.

grep -l "core type: two" *.txt > $1

#prints out the file that was written to
cat $1

 #if user inputs three 
elif [[ $coretype = "three" ]]
then

#prints some info
echo "Collecting data on type three"
echo "Here are the results: "
echo "Type three is the achiever"

#grep command to search for all files containing core type: three               
#also outputs the data from the grep command into a file passed in with the   
#positional parameter.

grep -l "core type: three" *.txt > $1
#prints out the file that was written to
cat $1
 
else

#this runs if user inputs core 4 and tells the user some info 
echo "Collecting data on type four"
echo "Here are the results: "
echo "Type four is the individualist"

#grep command to search for all files containing core type: four               
#also outputs the data from the grep command into a file passed in with the   
#positional parameter.

grep -l "core type: four" *.txt > $1

cat $1 
fi
