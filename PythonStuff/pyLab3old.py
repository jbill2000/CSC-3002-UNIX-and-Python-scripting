#! /usr/bin/env python3

def codonSearch(sequence, codonstring, startsearch):
	startlist=[]
	tagList=[]
	taaList=[]
	tgaList=[]
	finallist=[]
	startcount=0
	tagcount=0
	taacount=0
	tgacount=0
	for i in range(startsearch,len(sequence)-2,3):
		if sequence[i:i+3] == 'ATG' and codonstring == 'ATG':
			startcount=startcount+1 
			finallist.append(i)
		if sequence[i:i+3] == 'TAG' and codonstring == 'TAG':
			tagList.append(i)
			tagcount=tagcount+1 
		if sequence[i:i+3] == 'TAA' and codonstring == 'TAA':
			taaList.append(i)
			taacount=taacount+1
		if sequence[i:i+3] == 'TGA' and codonstring == 'TGA':
			tgaList.append(i)
			tgacount=tgacount+1
	if startcount > 0:
		print("There are no start codons ")
	if startcount > 1:
		finallist.append(startlist)
	if tagcount > 1:
		finallist.append(tagList)
	if taacount > 1:
		finallist.append(taaList)
	if tgacount > 1:
		finallist.append(tgaList)
	

		return finallist

sequence= input("Enter a DNA Sequence: ")
sequence= sequence.upper()

print("Start codons are found at the following locations: ")

print(codonSearch(sequence,'ATG',0))

print("Stop codons TAG are found at the following locations: ")
codonSearch(sequence, 'TAG',0)
print("Stop codons TAA are found at the following locations: ")
codonSearch(sequence, 'TAA',0)
print("Stop codons TGA are found at the following locations: ")
codonSearch(sequence, 'TGA',0)




