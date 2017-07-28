# # Project Euler - Problem 26
# # 1/25/17
import math
import re
from types import *

def CheckRepetition(NumStr):
     length = len(NumStr)
     m = re.search(NumStr[length-1] + '{100}', NumStr)
     if type(m) is NoneType:
          pass
     else:
          return 1
     MaxRange = int(math.ceil(length/2))
     for i in range(2, MaxRange+2):
          TestStr = NumStr[length-i:length]
          m = re.search(TestStr + TestStr +TestStr, NumStr)
          if type(m) is NoneType:
               pass
          else:
               return len(TestStr)
     return 0

MaxRepeats = 1
for Div in range(800,1000):
     Dividend = 1000
     ModVal = Dividend % Div
     Num = (Dividend - ModVal)/Div  
     Quotient = str(Num)

     Count = 0
     Repeats = 0
     while (Count < 4000):

          Dividend = ModVal*10
          ModVal = Dividend % Div
          Num = (Dividend - ModVal)/Div

          Quotient = Quotient + str(Num)
          Count = Count+1

     Repeats = CheckRepetition(Quotient)
     if Repeats == 0:
          print Div, Repeats
     if Repeats > MaxRepeats:
          MaxRepeats = Repeats
          print Div, Repeats
     
     #print Div, Quotient[2500-10:2500], Repeats