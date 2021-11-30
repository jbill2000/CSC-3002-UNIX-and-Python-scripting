#!/bin/sh
total=1
echo "Enter the base followed by the power (ex: 2 3)"
read base power
until test $power -eq 0
 do
	total=`expr $total \* $base`
	power=`expr $power - 1`
done
echo "The answer is $total"
