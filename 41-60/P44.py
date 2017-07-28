# Project Euler - Problem 44 
# 7/8/17

TestLength = 2000

# Make pentagonal numbers (length = TestLength):
P = []
for n in range(1, TestLength):
  Num = n*(3*n-1)/2
  P.append(Num)
# Make pentagonal numbers up to maximum sum:
Limit = P[-1] + P[-2]
while Num<=Limit:
  n+=1 
  Num = n*(3*n-1)/2
  P.append(Num)

# Find pairs with pentagonal sums and differences
for i in range(0, TestLength):
  j = i+1
  Found = False
  if (P.count(P[j]-P[i]) == 1) and (P.count(P[j]+P[i]) == 1):
     print(P[i], P[j], P[i]+P[j], P[j]-P[i])
  
  while (j<len(P)) and (Found == False):
    if (P.count(P[j]-P[i]) == 1) and (P.count(P[j]+P[i]) == 1):
      Found = True
      print(P[i], P[j], P[i]+P[j], P[j]-P[i])
    j+=1
  

