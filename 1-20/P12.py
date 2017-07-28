# Project Euler - Problem 12
# 1/8/17

import math

def FindFactors(n):
	Factors = [1, n]
	Top = math.ceil(math.sqrt(n))
	for i in range(2,int(Top)):
		if n%i == 0:
			Factor = n/i 
			Factors.append(i)
			Factors.append(Factor)
	return len(Factors)


PartialSum = 1
i = 1
length = 1
while i < 10000:
	i = i+1
	PartialSum = i+PartialSum
while i<15000: #length < 400:
	i = i+1
	PartialSum = i+PartialSum
	length = FindFactors(PartialSum)
	if length > 400:
		print i, PartialSum, length 
	
