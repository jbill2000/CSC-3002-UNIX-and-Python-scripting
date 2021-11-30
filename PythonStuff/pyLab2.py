#! /usr/bin/env python3
#asks user for name and year and stores them in variables
name=input("Please enter your name : ")

year=input("Please enter your year of birth : ")
 
id= name+'_'+year

#prints the id
print(id)

#calculates the age for later
age= 2021-int(year)

#the line we are testing them on remembering items from
test= "I went to the store and bought a pencil, an apple, a book, a bag, a stapler and a pillow" 
#takes in the user input   
userinput=input("What words do you remember? Please write them separated by spaces: ")
#counts the number of spaces +1
inputtotal= userinput.count(" ")+1
#sets count to 0
count=0

#counts the number of times a word was said
applenum= userinput.count("apple")
booknum= userinput.count("book")
bagnum= userinput.count("bag")
staplernum= userinput.count("stapler")
pillownum= userinput.count("pillow")
pencilnum= userinput.count("pencil")

#if any word counted was greater than 0 it will increment count by 1 for the total correct counts
if(applenum>0):
	count= count+1
if(booknum>0):
	count= count+1
if(bagnum> 0):
	count= count+1
if(staplernum > 0):
	count= count+1
if(pillownum > 0):
	count = count+1
if(pencilnum>0):
	count= count+1

#asks user for the longest word they can think of
longword= input("What is the longest word that you can think of? ")
#prints 
print("Patient %s came up with %s words and %s were correct" %(id,inputtotal,count))
#calculates percent for later
percent= 100* count/6
#tells user the percent right
print("This is %.2f percent of the words from the original sentence that were correct "%(percent))
#stores the length of the longest word and prints it 
longwordlen= len(longword)
print("The longest word the patient could come up with was %s characters" %(longwordlen))

#if statements that output various things depending on what number count is as well as user age
if(count == 6):
	print("Well done! There is no concern about the memory of patient %s" %(id))
elif(count == 5 or count == 4):
	print("Patient %s has a reasonable memory" %(id))
elif(count == 2 or count == 3):
	print("There is some concern about Patient %s memory "%(id))
	if(age >= 65):
		print("This could be due to age")
	elif(age < 65):
		print("Please conduct further testing on Patient %s for stress and depression"%(id))
elif(count <= 1):
	print("Further evaluation is definitely needed for Patient %s "%(id))
