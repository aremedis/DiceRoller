import random
import string

#define basic RNG
def ROLLER(NumSides):
	return random.randint(1,NumSides)

#define dice types
def d20():
	return ROLLER(20) 

def d10():
	return ROLLER(10) 

def d8():
	return ROLLER(8) 

def d6():
	return ROLLER(6) 

def d3():
	return ROLLER(3) 

def d2():
	return ROLLER(2)

#4d6 drop lowest
def droplowest(NumDice):
	attrib = []
	for die in range(0,NumDice):
		attrib.append(d6())
	attrib.remove(min(attrib))
	y = 0
	for x in attrib:
		y = y + x
	return attrib, y, #int((y-10)/2)

def DnDStats():
	StatArray = []
	for x in range(0,6):
		StatArray.append(droplowest(4))




###
# everything after this is trash and should be removed
###


#print (str(d20(d20mod))+" = " + "1d20 + "+ str(d20mod))

#for die in range(0,NumDice):
#	print (str(d6()))


#




StatArray = []
for x in range(0,6):
	StatArray.append(RollStats())

print (StatArray)