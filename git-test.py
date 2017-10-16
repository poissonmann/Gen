#gitisgit
#example output
#WIT IS GIT
#PIT IS GIT
#GIT IS BIT
#

#version 2: just cursive dictionary

import math
import random


def findG(gitstring):
	for i in range(len(gitstring)):
		if gitstring[i] == "G":
			indexG = i
			print(indexG)
			return indexG+1 #for now 1 is enough


def alters_ascii():
	pass


def sayXit(altnum=3):
	"""

	Modulates the G in Git to display the right amount of little something other 

	"""

	truthString = " GIT IS GIT"  #Do not alter
	print(truthString)
	
	Gplace = findG(truthString)
	print(Gplace)	
	for i in range(altnum):
				
		alters = ["P", "L", "W", "MOSPH", "B", "HI", "S", "F"]
		otherThanG = random.randint(0, len(alters)-1)
		
		print(truthString[1][0]+", "+alters[otherThanG]+truthString[Gplace:])
		



##Compute, translate to machineLanguage, export to binarial terms for the ALU to comprehend
## and amaze the terminal-end user for few modificications.
sayXit()


#__init__
#__main__
#__docstring__
