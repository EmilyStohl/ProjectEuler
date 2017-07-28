# Project Euler - Problem 17
# 1/8/17

OnesPlace = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13: 8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

TensPlace = {20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}
OneThousand = 11

Sum = 0
for i in range(1,20):
     Sum = Sum + OnesPlace[i];
for i in range(20, 100):
     Ones = i%10
     Tens = i-Ones
     Sum = Sum + OnesPlace[Ones] + TensPlace[Tens]

print Sum*10

# Hundreds: 100, 200, 300, 400, etc. 1000
Sum = 0
for i in range(1,10): 
     Sum = Sum + OnesPlace[i] + 7
print Sum + 11

#One hundred and ... Two hundred and 
Sum = 0
for i in range(1,10): 
     Sum = Sum + (OnesPlace[i] + 10)*99
print Sum


