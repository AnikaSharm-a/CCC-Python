# CCC 2013 S2 https://www.cemc.uwaterloo.ca/contests/computing/2013/stage1/seniorEn.pdf

maxweight = int(input())
numcars = int(input())
weights = [int(input()) for i in range(numcars)]
passed = 0
s = 0

# First 4 cars
for i in range(min(4, numcars)):
	s += weights[i]

	if s <= maxweight: passed += 1
	else: break

# cars after the first 4 passed
if passed == 4:

	for i in range(1, numcars - 3):
		totalweight = weights[i] + weights[i+1] + weights[i+2] + weights[i+3]

		if totalweight <= maxweight: passed += 1
		else: break

print(passed)