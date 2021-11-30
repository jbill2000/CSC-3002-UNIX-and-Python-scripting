#!/bin/bash
echo "Enter your four digit birthyear"
read year
echo "$year is a great year!"
curyear=2021
legal=21
if [[ $year -gt 2000 ]]

then
	curage=`expr $curyear - $year`
	yearsuntil=`expr $legal - $curage`
	result=$yearsuntil
	echo "You will be 21 in $result years"
else
	echo "You are at least 21!"
fi
