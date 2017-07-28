# Project Euler - Problem 10
# 1/8/17
import math
PrimeList = []

def isPrime(n):
	for k in PrimeList:
		if n%k == 0:
			return False
	PrimeList.append(n)
	return True

i = 3
Sum = 2
#count = 1
while i < 2000000:

	if isPrime(i) == True:
		Sum = Sum+i
	i = i+2
	if i%100000 == 1:
		print i
print Sum