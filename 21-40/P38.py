# Project Euler - Problem 38 
# 3/4/2017

def CheckPan(NumberString):
  if len(NumberString) != 9:
    return False
  if NumberString.count('0') != 0:
    return False
  if NumberString.count('1') != 1:
    return False
  if NumberString.count('2') != 1:
    return False
  if NumberString.count('3') != 1:
    return False
  if NumberString.count('4') != 1:
    return False
  if NumberString.count('5') != 1:
    return False
  if NumberString.count('6') != 1:
    return False
  if NumberString.count('7') != 1:
    return False
  if NumberString.count('8') != 1:
    return False
  if NumberString.count('9') != 1:
    return False
  return True

PanNums = []

for i in range(1, 100000):
  # Check if i starts with 9
  Num = str(i)
  if Num[0]=='9':
    Length = len(Num)
    Multiplier = 2
    while Length < 9:
      Num = Num + str(Multiplier*i)
      Multiplier = Multiplier+1
      Length = len(Num)
    if Length == 9:
      if CheckPan(Num) == True:
        PanNums.append(Num)

PanNums.sort()        
print PanNums