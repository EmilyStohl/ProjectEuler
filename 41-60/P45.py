# Proect Euler - Problem 45 
# 8/6/17
import math

def CheckQuadraticEq(a, b, c):
  Root = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
  # Check if root is an integer
  return abs(round(Root)-Root) < 0.00001
 

def IsPentNum(Num):
  # Use quadratic equation to check if some n where Num == n(3n-1)/2
  a = 3
  b = -1
  c = -Num*2
  return CheckQuadraticEq(a, b, c)
   
  
def IsTriNum(Num):  
  # Use quadratic equation to check if some n where Num == n(3n-1)/2
  a = 1
  b = 1
  c = -Num*2
  return CheckQuadraticEq(a, b, c)


#calculate hex numbers, check if also pentagonal number and triangle number
FoundCount = 0
n = 1
while FoundCount < 3:
  hexNum =  n * (2*n-1)
  if (IsTriNum(hexNum) == True) and (IsPentNum(hexNum) == True):
    print n, hexNum
    FoundCount += 1
  n+=1

  


