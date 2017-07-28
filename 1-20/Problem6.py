# Project Euler - Problem 6

Sum = 0
for i in range(1,101):
	Sum = Sum+i
SquareSum = Sum*Sum 

Sum = 0
for i in range(1,101):
	Sum = i*i + Sum
	
print(SquareSum - Sum)