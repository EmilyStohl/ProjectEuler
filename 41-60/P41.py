# Project Euler - Project 41
# 7/2/2017
import math

# Create pandigital numbers
# Check if each number is prime

n = 9


def isPrime(n, PrimeList):
	for k in PrimeList:
		if n%k == 0:
			return False
	PrimeList.append(n)
	return True

# Create pandigital numbers
PanNums = ['1', '3', '5', '7', '9']
PrimeList = [2]

for i in range(2, n+1):
	Temp = []
	for spot in PanNums:
		for j in range(1, n+1):
			Add = str(j)
			if spot.count(Add) == 0:
				Temp.append(Add+spot)
	PanNums = Temp
#print PanNums
print("Step 1 done")

for i in range(0, len(PanNums)):
	Num = PanNums.pop()
	print Num
	if isPrime(int(Num)) == True:
		print Num
	

