# Project Euler - Problem 27
# 1/10/17
import math

def TestPrime(n):
	Top = math.ceil(math.sqrt(n))
	for i in range(2,int(Top)+1):
		if n%i == 0:
			return False
	return True
	

MaxN = 0
MaxA = -2000
MaxB = -2000
for a in range(-999, 1000):
	for b in range(-1000, 1001):
		Stop = False
		n = 0
		while Stop == False:
			TestNum = n**2+(a*n)+(b)
			if TestNum < 2:
				Stop = True
			else:
				if TestPrime(TestNum) == True:
					if n > MaxN:
						MaxN = n
						MaxA = a
						MaxB = b
				else:
					Stop = True
			n = n+1
			
print MaxA*MaxB
print MaxN
print MaxA, MaxB
