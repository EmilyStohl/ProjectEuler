# Project Euler - Problem 40
# 3/4/2017

NumStr = "1"
for i in range(2, 1000000):
  NumStr = NumStr + str(i)
  
print NumStr[0]
print NumStr[9]
print NumStr[100-1]
print NumStr[1000-1]
print NumStr[10000-1]
print NumStr[100000-1]
print NumStr[1000000-1]