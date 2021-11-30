#!/usr/bin/env python3
#codon search function that returns a list
def codonSearch(sequence, codonstring, startsearch):
	#creates list
	list= []
	#for loop that searches through the sequence 
	for i in range(startsearch,len(sequence)-2):
		#different if statements that will execute depending on the string found and the codon string passed in
		if sequence[i:i+3] == 'ATG' and codonstring == 'ATG':
			list.append(i)
		if sequence[i:i+3] == 'TAG' and codonstring == 'TAG':
			list.append(i)
		if sequence[i:i+3] == 'TAA' and codonstring == 'TAA':
			list.append(i)
		if sequence[i:i+3] == 'TGA' and codonstring == 'TGA':
			list.append(i)

	return list
#takes in a sequence from the user and converts it into uppercase
sequence= input("Enter a DNA Sequence: ")
sequence= sequence.upper()
#creates the various lists 
startList=[]
tagList=[]
taaList=[]
tgaList=[]
#fills startList with the list returned from the function
startList=codonSearch(sequence,'ATG',0)
#if the len of startList is 0 there are no start codons and we want to execute the program 
if len(startList)== 0:
	print("There are no start codons")
	exit()
#else it will search the rest of the sequence and start from the first start codon location
else:
	starter=startList[0]	
	tagList= codonSearch(sequence,'TAG',starter)
	taaList= codonSearch(sequence, 'TAA',starter)
	tgaList= codonSearch(sequence, 'TGA',starter)

#prints start codons
print("Start codons are found at the following locations: ")

for i in range(len(startList)):
		print(startList[i])
#prints stop codons
print("Stop codons TAG  are found at the following locations: ")

if len(tagList) > 0:
	for i in range(len(tagList)):
		print(tagList[i])
else:
	print(" ")
#prints stop codons
print("Stop codons TAA  are found at the following locations: ")
if len(taaList) > 0:
	for i in range(len(taaList)):
		print(taaList[i])
else:
	print(" ")
#prints stop codons	
print("Stop codons TGA  are found at the following locations: ")

if len(tgaList) > 0:
	for i in range(len(tgaList)):
		print(tgaList[i])

else:
	print(" ")
#variable for use later
modcalc=0

#nested for loops for finding the ORF's with start val and the TAG codons
for i in range(len(startList)):
	#if there is anything in the list
	if len(tagList) > 0:
		for j in range(len(tagList)):
			#if startLists val is less than Tag then execute. This is here so it only looks from start to stop
			if startList[i] < tagList[j]:
				#calculates a val for modulus
				modcalc= tagList[j]-startList[i]
				modcalc= modcalc % 3
				#if modcalc is 0 then its an potential ORF and will print it
				if modcalc == 0:
					print("Potential ORF starting at %d ending at %d " % (startList[i], tagList[j]))

#nested for loops for finding the ORF's with start val and the TAA codons
for i in range(len(startList)):
	#if the list isnt empty do the rest
	if len(taaList) > 0:
		for j in range(len(taaList)):
			#if startLists val is less than Taa then execute. This is here so it only looks from start to stop
			if startList[i] < taaList[j]:
				#calculates variable for modulus
				modcalc= taaList[j]-startList[i]
				modcalc= modcalc % 3
				#if modcalc is 0 then its an potential ORF and will print it.
				if modcalc == 0:
					print("Potential ORF starting at %d ending at %d " % (startList[i], taaList[j]))

#nested for loops for finding the ORF's with start val and the TAG codons
for i in range(len(startList)):
	#if the list isnt empty then do the rest
	if len(tgaList) > 0:
		for j in range(len(tgaList)):
			#if the val of start is less than tga then execute. This is needed to only look at start to stop.
			if startList[i]<tgaList[j]:
				#calculates mod calc for later use 
                        	modcalc= tgaList[j]-startList[i]
                        	modcalc= modcalc % 3
                                #if modcalc is 0 then its an potential ORF and will print it
                        	if modcalc == 0:
                               			print("Potential ORF starting at %d ending at %d " % (startList[i], tgaList[j]))
