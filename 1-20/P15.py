# Project Euler - Problem 15
# 4/28/17


Size = 20
Matrix = [[0 for x in range(Size+1)] for y in range(Size+1)] # Make 21x21 matrix

for i in range(1, Size+1):
  Matrix[i][0] = 1
  Matrix[0][i] = 1
for row in range(1, Size+1):
  for col in range(1, Size+1):
    Matrix[row][col] = Matrix[row-1][col]  + Matrix[row][col-1]
    
print Matrix[Size][Size]

## Old way: (Takes too long to run for Size = 20)

# Size = 3
# PosList = [[0,0]]
# PathCount = 0 

# while len(PosList) > 0:
#   Spot =  PosList.pop()
#   if (Spot[0] == Size) or (Spot[1] == Size):
#     PathCount = PathCount+1
#   else:
#     if Spot[0] < Size:
#       PosList.append([Spot[0]+1, Spot[1]])
#     if Spot[1] < Size:
#       PosList.append([Spot[0], Spot[1]+1])

# print PathCount