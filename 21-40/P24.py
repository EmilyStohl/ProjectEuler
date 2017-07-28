# Project Euler - Problem 24
# 5/19/2017

n = 9
PanNums = []

for i in range(0, n+1): 
	PanNums.append(str(i))
for i in range(1, n+1):
	Temp = []
	for spot in PanNums:
		for j in range(0, n+1):
			Add = str(j)
			if spot.count(Add) == 0:
				Temp.append(spot+Add)
	PanNums = Temp

print PanNums[1000000-1]