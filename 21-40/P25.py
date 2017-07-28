# Project Euler - Problem 25
# 1/8/17

a = 1 
b = 1

Found = False
index = 2
while Found == False:
	c = a+b
	a = b
	b = c
	index += 1
	if len(str(c)) == 1000:
		Found = True
		print index

	
	
	
