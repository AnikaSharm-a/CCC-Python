# CCC 2012 S2 https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

def getbase(l):
	if l == "I": base = 1
	elif l == "V": base = 5
	elif l == "X": base = 10
	elif l == "L": base = 50
	elif l == "C": base = 100
	elif l == "D": base = 500
	elif l == "M": base = 1000
	return base

def minus(currentletter, nextletter):
	if letters.index(nextletter) > letters.index(currentletter): y = -1
	else: y = 1

	return y


letters = ["I", "V", "X", "L", "C", "D", "M"]
chars = list(input())
groups = []
decimal = 0

for i in range(0,len(chars),2):
	groups.append(chars[i:i+2])


for i in range(len(groups)-1):
	num = int(groups[i][0])
	letter1 = groups[i][1]
	letter2 = groups[i+1][1]

	decimal += num*getbase(letter1)*minus(letter1, letter2)


decimal += int(groups[i+1][0])*getbase(groups[i+1][1])

print(decimal)