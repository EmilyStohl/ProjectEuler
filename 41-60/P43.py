# Project Euler - Problem 43
# 7/2/17

def TestSubstrings(num): # test for 3-digit substring divisibility by primes
	Prime = [1, 2, 3, 5, 7, 11, 13, 17]
	for i in range(1, 8):
		testNum = int(num[i:i+3])
		if testNum % Prime[i] != 0:
			return False
	return True

def MakePanNums(n): # create all 0 to n pandigital numbers
	PanNums = []
	for i in range(0, n+1): 
		PanNums.append(str(i))
	for i in range(1, n+1):
		Temp = []
		for spot in PanNums:
			for j in range(0, n+1):
				Add = str(j)
				if spot.count(Add) == 0:
					Temp.append(spot+Add)
		PanNums = Temp
	return PanNums

###

n = 9
AllPans = MakePanNums(n)



Sum = 0 # Will add all numbers that have sub-string divisibilty 	
for number in AllPans:
	if TestSubstrings(number) == True:
		print(number)
		Sum = Sum + int(number)
	
print Sum
	
	