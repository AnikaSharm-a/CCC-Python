# CCC 2009 S1 https://www.cemc.uwaterloo.ca/contests/computing/2009/stage1/seniorEn.pdf

# cannot be solved with python- TLE in cases 2 and 5

from math import sqrt

lower = int(input())
upper = int(input()) + 1
counter = 0

for i in range(lower, upper):
	cube = i**(1/3)

	if (cube - int(cube) > 0.999 or cube % 1 == 0.0) and sqrt(i) % 1 == 0.0: counter += 1

print(counter)