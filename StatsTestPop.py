# This program was designed to test whether a large difference in sample sizes actually made
# a difference in how statistically comparable two sample sets were.
# Author: Collin Mitchell
#   Date: 2015 13th Fedruary   | FRIDAY THE THIRTEENTH. WOO.

# ..self.
def randomSort(tempList):
	import random as r
	r.shuffle(tempList)
	return tempList

# We don't have the real results form the survey, but we don't need them since we've been given percentages and the total number. Hence,
# we can calculate the real numbers from that. The real issue is that there will be partial people. And, there is no "great" solution to this.
# But for simplicity sake, I will floor the numbers to remove the excess "partial people." 
def generateManList():
	import math as m

	# Total Size
	men      = 375
	tempList = []

	mEight = m.floor(men * .136) # 13.6 %
	mSeven = m.floor(men * .405) # 40.5 %
	mSix   = m.floor(men * .144) # 14.4 %
	mFive  = m.floor(men * .120) # 12.0 %
	mFour  = m.floor(men * .069) # 6.90 %
	mThree = m.floor(men * .101) # 10.1 %
	mTwo   = m.floor(men * .016) # 1.60 %
	mOne   = m.floor(men * .003) # .300 %
	mZero  = m.floor(men * .005) # .500 %

	# I'm too lazy right now to turn this into it's own subfunction.
	# Yes, all of this can be stuffed into a single function to remove repetitive code.
	# No, I'm not going to do it because this code is finished and does what I need it to do.
	# Yes, it's ugly: dealwithit.jpg.
	for val in range(1, int(mEight+1)):
		tempList.append(8)

	for val in range(1, int(mSeven+1)):
		tempList.append(7)

	for val in range(1, int(mSix+1)):
		tempList.append(6)

	for val in range(1, int(mFive+1)):
		tempList.append(5)

	for val in range(1, int(mFour+1)):
		tempList.append(4)

	for val in range(1, int(mThree+1)):
		tempList.append(3)

	for val in range(1, int(mTwo+1)):
		tempList.append(2)

	for val in range(1, int(mOne+1)):
		tempList.append(1)

	for val in range(1, int(mZero+1)):
		tempList.append(0)

	
	return tempList

# ..self
def arrayPicker(tempList):
	import random as r
	tempArray = []

	# For each run, pull a random element from the full sample space.
	# Then, deposit it in the real sample.
	# Note: There are a total of 187 females, so we pull 187 elements from the list to match the sample size
	for x in range(187):
		randomIndex = r.randint(0, len(tempList)-1)
		tempArray.append(tempList[randomIndex])

	return tempArray

# ..self
def historgram(tempList):
	# Python has no switch statement, so this is going to be really ugly.
	# This is less of a "Show off my code" moment anyways.
	zero  = 0
	one   = 0
	two   = 0
	three = 0
	four  = 0
	five  = 0
	six   = 0
	seven = 0
	eight = 0

	for item in tempList:
		if   item is 0: zero  = zero  +1
		elif item is 1: one   = one   +1
		elif item is 2: two   = two   +1
		elif item is 3: three = three +1
		elif item is 4: four  = four  +1
		elif item is 5: five  = five  +1
		elif item is 6: six   = six   +1
		elif item is 7: seven = seven +1
		else          : eight = eight +1

	return [zero, one, two, three, four, five, six, seven, eight]

#...self
def generateResult(men, women, sample):
	string =          "  %12s %6s %12s %6s %12s" % ("Men Base", " ", "Men Sample", " ", "Female Base\n")
	string = string + "  %13s %6s %12s %6s %12s" % ("-"*13, " ", "-"*12, " ", "-"*12 + "\n")

	for x in range(9):
		string = string + str(x) + ": %12.2f %6s %12.2f %6s %12.2f" % (men[x], " ", 100 * sample[x], " ", women[x])
		string = string + "\n"
	return string
	



#...self
def compareData(tempList):
	womenData = {8: 5.3,  7: 19.3, 6: 11.2, 5: 17.1, 4: 18.7, 3: 21.4, 2: 4.8, 1: 1.6, 0: .5}
	menData   = {8: 13.6, 7: 40.5, 6: 14.4, 5: 12,   4: 6.9,  3:10.1,  2: 1.6, 1: .3,  0: .5}

	# store the data for comparison.
	# Remeber that '/' is integer division and drops the decimals!
	sampleData = {}
	sampleData[8] = tempList[8] /187.0
	sampleData[7] = tempList[7] /187.0
	sampleData[6] = tempList[6] /187.0
	sampleData[5] = tempList[5] /187.0
	sampleData[4] = tempList[4] /187.0
	sampleData[3] = tempList[3] /187.0
	sampleData[2] = tempList[2] /187.0
	sampleData[1] = tempList[1] /187.0
	sampleData[0] = tempList[0] /187.0

	return generateResult(menData, womenData, sampleData)

# If run via commandline, run the program
if __name__ == "__main__":
	import sys
	manList       = generateManList()
	manListSorted = randomSort(manList)

	sampleList    = arrayPicker(manListSorted)

	histoData     = historgram(sampleList)
	results       = compareData(histoData)
	print results
