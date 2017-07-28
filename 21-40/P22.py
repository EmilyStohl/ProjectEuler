# Project Euler - Problem 22
# 1/8/17
import csv

file = csv.reader(open("Names.txt", 'r'), delimiter=',')

for row in file:
     List = row
List.sort()

LetterDict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

Pos = 1
Total = 0
for Name in List:
     NameSum = 0
     for Letter in Name:
          NameSum = NameSum + LetterDict[Letter]
     Total = NameSum*Pos + Total
     Pos = Pos+1
     
print Total