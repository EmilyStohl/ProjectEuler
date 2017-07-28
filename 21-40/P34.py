# Project Euler - Problem 34
# 2/16/17

import math

FactTable = [1, 1, 2, 6, 24, 120,720,5040,40320,362880 ] 

Sum = 0
for a in range(145, 100000):
	NumStr = str(a)
	NumSum = 0
	for i in range(0, len(NumStr)):
		digit = int(NumStr[i])
		NumSum = NumSum + FactTable[digit]
	if NumSum == a:
		print a
		Sum = Sum + a
print Sum 

		   
   