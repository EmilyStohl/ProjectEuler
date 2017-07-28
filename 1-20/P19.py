# Project Euler - Problem 19
# 1/8/17

MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Year = 1901
Month = 1

Num = 2 # Day Number: Sun 0 Mon 1 Tues 2 ...
Count = 0

while Year < 2001:
	Num = Num + MonthDays[Month-1]
	if (Year%4 == 0) and (Month == 2):
		Num = Num+1
	# Check if Sunday:
	if Num%7 == 0:
		Count = Count+1	
	# Iterate through year, month
	Month = Month+1
	if Month == 13:
		Month = 1
		Year = Year+1
print Count
