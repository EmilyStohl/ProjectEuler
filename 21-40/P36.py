# Project Euler - Problem 36
# 2/17/2017

import math

def BinConvert(x):
     return str(bin(x)[2:])

def TestPalindrome(x):
     n = str(x)
     length = len(n)
    
     for j in range(0, int(math.ceil(length/2))):
          if n[j] != n[length-j-1]:
               return False
     return True
 
Sum = 0      
for i in range (1, 1000000):
     if TestPalindrome(i) and TestPalindrome(BinConvert(i)):
          print i , BinConvert(i)
          Sum = Sum + i 
print "Sum:", Sum          




