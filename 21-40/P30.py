# Project Euler - Problem 30
# 2/16/17
import math

Sum = 0
for a in range(4000, 1000000):
	NumStr = str(a)
	NumSum = 0
	for i in range(0, len(NumStr)):
		NumSum = NumSum + int(NumStr[i])**5
	if NumSum == a:
		print a
		Sum = Sum + a
print Sum 
