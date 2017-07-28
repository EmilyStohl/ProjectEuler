# Project Euler - Problem 3
import math

def isPrime(n, PrimeList):
	for k in PrimeList:
		if n%k == 0:
			return False
	PrimeList.append(n)
	return True

Num = 600851475143

PrimeList = [2]
i = 3
while i < math.ceil(math.sqrt(Num)):
  if isPrime(i, PrimeList) == True: # Check if prime
    if Num%i == 0: # Check if factor of num
      Factor = Num/i 
      print i, Factor
  i = i+1




        