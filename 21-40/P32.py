# Project Euler - Problem 32
# 3/3/2017

def CheckPan(p1, p2, Prod):
  NumberString = str(p1) + str(p2) + str(Prod)
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

ProdList = []
for p1 in range(1, 2000):
  for p2 in range(p1, 2000):
    Prod = p1*p2
    if CheckPan(p1, p2, Prod) == True:
      print p1, p2, Prod
      ProdList.append(Prod)
      

NewList = list(set(ProdList))
print sum(NewList)