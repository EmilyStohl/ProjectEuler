# Project Euler - Problem 42
# 5/29/2017

## Import word.txt
import csv
file = csv.reader(open("words.txt", 'r'), delimiter=',')

for row in file:
	List = row

## Create list of triangle numbers
TriangleNums = []
for n in range(1, 100):
	Num = n*(n+1)/2
	TriangleNums.append(Num)
	
## Calculate word value for each word, check if traingle number
LetterDict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

WordCount = 0
for word in List:
	WordValue = 0
	for letter in word:
		WordValue = WordValue + LetterDict[letter]
	
	if TriangleNums.count(WordValue)	== 1:
		print word, WordValue
		WordCount += 1

		
		
print WordCount		