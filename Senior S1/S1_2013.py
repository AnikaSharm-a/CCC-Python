# CCC 2013 S1 https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/seniorEn.pdf

year = int(input()) + 1

def distinctyear(x):
	x = str(x)
	useddigits = []

	for i in x:
		if i in useddigits: return False
		useddigits.append(i)

	return True

while not distinctyear(year):
	year += 1

print(year)