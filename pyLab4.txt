#! /usr/bin/env python3
import re
proteinDict= {'TTT':'Phe','TCT':'Ser','TAT':'Tyr','TGT':'Cys',
'TTC':'Phe','TCC':'Ser','TAC':'Tyr','TGC':'Cys',
'TTA':'Leu','TCA':'Ser','TAA':'STOP','TGA':'STOP',
'TTG':'Leu','TCG':'Ser','TAG':'STOP','TGG':'Trp',
'CTT':'Leu','CCT':'Pro','CAT':'His','CGT':'Arg',
'CTC':'Leu','CCC':'Pro','CAC':'His','CGC':'Arg',
'CTA':'Leu','CCA':'Pro','CAA':'Gln','CGA':'Arg',
'CTG':'Leu','CCG':'Pro','CAG':'Gln','CGG':'Arg',
'ATT':'Ile','ACT':'Thr','AAT':'Asn','AGT':'Ser',
'ATC':'Ile','ACC':'Thr','AAC':'Asn','AGC':'Ser',
'ATA':'Ile','ACA':'Thr','AAA':'Lys','AGA':'Arg',
'ATG':'Met','ACG':'Thr','AAG':'Lys','AGG':'Arg',
'GTT':'Val','GCT':'Ala','GAT':'Asp','GGT':'Gly',
'GTC':'Val','GCC':'Ala','GAC':'Asp','GGC':'Gly',
'GTA':'Val','GCA':'Ala','GAA':'Glu','GGA':'Gly',
'GTG':'Val','GCG':'Ala','GAG':'Glu','GGG':'Gly',}


#function to check if there is invalid characters in the sequence
def seqCheck(sequence):
	theSet=set()
	#if there is any character except a upper or lowercase a g c or t it will add it to the set
	for i in range(len(sequence)):
		if sequence[i] != 'a' and sequence[i] != 'g' and sequence[i] != 'c' and sequence[i] != 't' and sequence[i]!='A' and sequence[i]!='G' and sequence[i]!='C' and sequence[i]!='T':
			theSet.add(sequence[i])
	#returns the set
	return theSet
#function to print the amino acid from the dict
def aminoAcid(sequence,proteinDict):
	list = []
	i=0
	#for loop to look for slices of 3, if codon is a slice of 3 it will add it to the list and get the dict val
	for i in range(i,len(sequence),3):
		codon= sequence[i:i+3]
		list.append(proteinDict.get(codon,'-'))
		
	
	return list

#searches for restriction sites, takes in the sequence and a list of the sites
def restrictionSearch(restrictionsequence,site):
	#variables
	i=0
	counter=0
	#loops through each of the restriction sites	
	for i in range(len(site)):
		#sets variables id and locator = to 0 each time through
		id=0
		locater=0
		#loops through the whole sequence in search of the restriction site
		for j in range(len(restrictionsequence)):
			#if a restriction site is found for the first time it will print where it was found
			if restrictionsequence[locater:locater+len(site[i])] ==site[i] and id==0:
				print(site[i],"was found at",j)
				#increments id so the same site cant be found again
				id=id+1
				#counter to keep track of how many sites are found
				counter=counter+1
			locater=locater+1
		#if id is 0 then it was not found and it will print 
		if(id==0):
			print(site[i],"was not found")
	#this prints how many sites were found
	print(counter,"restriction sites were found")	
		
	
			
#menu
print("Choose an activity ")
print("1: Print the current DNA sequence")
print("2: Print the related amino acids")
print("3: Input a new DNA sequence")
print("4: Look for restriction site")
print("5: Read a new sequece from a new FASTA file")
print("q: Quit the program")
#variables
sequence=""
choice='p'
#while choice is not q it will loop through 
while(choice != 'q'):
	#asks for choice at the beginning of the loop only
	choice=input("Choice: ")
	#if there is no sequence in it will print there was no sequence
	if choice == '1' and len(sequence) == 0:
		print("No sequence entered yet")
	#if a valid sequence is entered it will print the said sequence
	elif choice == '1' and len(sequence) > 0:  
		print(sequence)
	#same as the earlier if, if no sequence is in yet then it will print so
	elif choice == '2' and len(sequence) == 0:
		print("No sequence entered yet")
	#will print the matches of the sequence from the dictionary of proteins 
	elif choice == '2' and len(sequence) > 0:
		acidList=aminoAcid(sequence,proteinDict)
		for i in range(len(acidList)):
			print(acidList[i],end=" ")
		print("")
	#if choice is 3 it will take in a new sequence
	elif choice == '3': 
		sequence=input("Enter the new DNA sequence: ")
		#checks the sequence for any bad chars
		checkset=seqCheck(sequence)
		#if there are no bad characters then it converts it all to uppercase and is good to go
		if(len(checkset) == 0):
			sequence=sequence.upper()
		#if there are bad characters it will print them and prompt the user to try again
		else:
			print("Invalid sequence, new sequence not accepted")
			print("The following bad characters were found: ")
			
			for i in checkset:
				print(i,end=" ")
		print("\n")
	#if choice is 4 it will take in the restriction vals
	elif choice == '4':
		restriction=input("Input all of the restriction sites you wish to look for seperated by : ")
		restlist=[]
		#fills restlist by splitting the sites by the colon
		restlist= restriction.split(":")
		restrictionSearch(sequence,restlist)
	#if choice is 5	takes in a file and makes sure its a valid sequence	
	elif choice == '5':
		#gets the filename and opens it
		filename= input("From which file would you like to read? ")
		file= open(filename,'r')
		#reads in the file to sequence
		sequence=file.read()
		#regular expressions to modify the sequence and get rid of anything that shouldn't be there
		modstring= re.sub(r'\>\w+\s+\w+\s+\w+\s+\w+\-\w+\s+\w+','',sequence)
		modstring=re.sub(r'\s+',"",modstring)
		#sets sequence to the modified version
		sequence=modstring
		#runs sequence into the checker
		checker=seqCheck(sequence)
		#if its empty then its valid, if its invalid it will print that and tell the user to try again.
		if(len(checker)==0):	
			print("new sequence accepted")
		else:
			print("Invalid sequence, new sequence not accepted")
			print("The following bad characters were found: ")
			for i in checker:
				print(i,end=" ")
			print("\n")
	#if choice is q then quits
	elif choice == 'q':
		print("good-bye")
		quit()
	else:
		print("invalid choice, try again")
		
	
