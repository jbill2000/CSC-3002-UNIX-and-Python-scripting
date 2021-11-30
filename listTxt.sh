#!/bin/bash

#defines count to be incremented later
count=1

#for loop that gives FILE a new val each time it completes
for FILE in *.txt
do
	#print the num in front of file and print file
	echo $count $FILE
	#increment count by 1
	((count=count+1))
done 
