# Project Euler - Problem 48
# 8/6/17

Sum = 0

for i in range(1, 11):
  digitsStr = str(i**i)
  Sum = Sum + i**i

SumStr = str(Sum)
for i in range(11, 1001):
  digitsStr = str(i**i)
  if len(digitsStr) > 10:
    digitsStr = digitsStr[-10:]
  Sum = int(SumStr) + int(digitsStr)
  SumStr = str(Sum)
  if len(SumStr) > 15:
    SumStr = SumStr[-10:]

print SumStr

