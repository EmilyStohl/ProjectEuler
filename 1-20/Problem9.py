import math

for a in range (1,1000):
	for b in range(1,500):
		c = math.sqrt(pow(a,2)+pow(b,2))
		Check = a + b + c
		if math.fabs(Check - 1000) < 0.0001:
			print a,b,c
			
		