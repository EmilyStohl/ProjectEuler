# Project Euler - Problem 20
# 1/8/17

Prod = 1
for i in range(1,100):
	Prod = Prod*i
	
Num = str(Prod)
Sum = 0
for i in Num:
	Sum = Sum + int(i)
	
print Sum