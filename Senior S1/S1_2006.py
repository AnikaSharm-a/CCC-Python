# CCC 2006 S1 https://www.cemc.uwaterloo.ca/contests/computing/2005/stage1/seniorEn.pdf

t = int(input())
numbers = []

for i in range(t):
	num = input()
	numbers.append(num)

def turnchartonum(char):
	if char == "A" or char == "B" or char == "C": return "2"
	elif char == "D" or char == "E" or char == "F": return "3"
	elif char == "G" or char == "H" or char == "I": return "4"
	elif char == "J" or char == "K" or char == "L": return "5"
	elif char == "M" or char == "N" or char == "O": return "6"
	elif char == "P" or char == "Q" or char == "R" or char == "S": return "7"
	elif char == "T" or char == "U" or char == "V": return "8"
	elif char == "W" or char == "X" or char == "Y" or char == "Z": return "9"
	elif char == "-": return ""
	else: return char

newnums = []

for item in numbers:
	number = ""

	while len(number) < 10:
		for c in item:
			i = turnchartonum(c)
			number += i
		newnums.append(number)

finals = []

for num in newnums:
	part1 = num[0:3]
	part2 = num[3:6]
	part3 = num[6:10]
	finals.append(part1 + "-" + part2 + "-" + part3)

for final in finals:
	print(final)