# Project Euler - Problem 10
# 1/8/17
import math
PrimeList = [2]

def isPrime(n):
	for k in PrimeList:
		if n%k == 0:
			return False
	PrimeList.append(n)
	return True

i = 3
while i < 1000000:
	isPrime(i)
	i = i+1

count = 0
for prime in PrimeList:
	num = str(prime)
	length = len(num)
	
	if length == 1:
		count = count + 1
		
		
	else:
		IsCircular = True
		shift = 1
		OtherPrimes = []
		while (IsCircular == True) and (shift < length):
			NewNum = num[shift:length] + num[0:shift]
			if PrimeList.count(int(NewNum)) < 1:
				IsCircular = False
			shift = shift + 1
		if IsCircular == True:
			print prime
			count = count + 1 

			
print "Count:", count
