# Project Euler - Problem 37
# 3/3/2017
import math

PrimeList = [2, 3, 5, 7]

def isPrime(n):
	for k in PrimeList:
		if n%k == 0:
			return False
	PrimeList.append(n)
	return True

def CheckPrime(num):
	n = str(num)
	size = len(n)
	if PrimeList.count(int(n[0])) != 1:
		return False
	if PrimeList.count(int(n[size-1])) != 1:
		return False
	for p in range(1, size-1):
		n1 = int(n[0:size - p])
		n2 = int(n[p:size])
		if PrimeList.count(n1) != 1:
			return False
		if PrimeList.count(n2) != 1:
			return False
		
	return True



i = 11
TruncPrimeCount = 0
Sum = 0
while TruncPrimeCount < 11:
	if isPrime(i) == True:
		if CheckPrime(i) == True:
			TruncPrimeCount = TruncPrimeCount + 1
			print i 
			Sum = Sum + i 
	i = i+1

print Sum

