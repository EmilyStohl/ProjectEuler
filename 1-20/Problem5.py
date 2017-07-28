# Project Euler - Problem 5 

def Test(i):
	for p in range(2,21):
		if i%p != 0:
			return False
	print i
	return True


Found = False
n = 2520
while Found == False:
	Found = Test(n)
	n = n+20
	