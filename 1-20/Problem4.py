# Project Euler - Problem 4

for i in range(900, 1000):
	for k in range(900,1000):
		A = str(i*k)
		B = A[::-1]
		if A==B:
			print i,k
			print A
	

	