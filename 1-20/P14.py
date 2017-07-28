# Project Euler - Problem 10
# 1/8/17

def Collatz(a):
	count = 1
	while a > 1:
		if a%2 == 0:
			a = a/2
		else:
			a = 3*a + 1
		count = count + 1
	return count


Max = 0
MaxNum = 0
for i in range(1,1000000):
	Count = Collatz(i)
	if Count > Max:
		Max = Count
		MaxNum = i
		
print MaxNum