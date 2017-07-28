# Project Euler - Problem 29
# 2/16/17
import math

List = []
for a in range(2, 101):
	for b in range(2, 101):
		Num = a**b
		if List.count(Num) == 0:
			List.append(Num)
			
			

print len(List)