# Project Euler - Problem 23
# 1/8/17

def FindFactors(n):
	Factors = [1]
	Top = int(n/2)
	for i in range(2,Top+1):
		if n%i == 0:
			Factor = n/i 
			Factors.append(Factor)
			Factors.append(i)
	return sum(set(Factors))

# def CheckAbundantSum(n):
# 	index = 0 
# 	k = Abundant[index]
# 	while k < n:
# 		if Abundant.count(n-k) == 1:
# 			return True
# 		index = index + 1
# 		k = Abundant[index]
# 	return False

Set = range(1, 28123)

	
Abundant = []
for i in range(1,28123):
	b = FindFactors(i)
	if b	> i:
		Abundant.append(i)
		for Item in Abundant:
			Sum = i + Item
			if Set.count(Sum) == 1:
				Set.remove(Sum)
				print Sum
print Set
print sum(Set)	

# Sum = 0
# for i in range(1, 24):
# 	Sum = Sum + i
# for i in range(24,50):
# 	if CheckAbundantSum(i) == False:
# 		print i
# 		Sum = Sum+i
# print Sum
		
	
	
	
	
	
	