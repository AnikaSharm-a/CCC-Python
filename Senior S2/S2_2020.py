# CCC 2020 S2: https://cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf

# Beginner Approach - Depth First Search From (1, 1) to (M, N)

"""
Notes on the problem:

Pitfalls:
 - infinite loops ==> If the path loops on itself, you will loop infinitely
  - redoing work ==> If a path goes to a cell that has already been searched we are redoing work. (Solved with dynamic programming)
 - recursion depth ==> Annoying feature of python, can somewhat be solved with the hack shown in the first 2 lines of code
  - redoing factor work ==> there are only 1000 x 1000 numbers maximum, so would should only have to compute that many factors anyway.
  - overdoing factor work ==> We eliminated the amount of factorization by realizing that outputs beyond M or N are useless. (Otherwise they could give us a bunch of large numbers <= 10^6 to waste our time)

"""

import sys
sys.setrecursionlimit(100000)

from math import sqrt

M = int(input()) # num rows
N = int(input()) # num columns
lower_bound_factor = min(M, N)
upper_bound_factor = max(M, N)
grid = []

mem = {}

factors_mem = {}

for nums in range(M):
	grid.append(list(map(int, input().split(" "))))

def getFactors(x):
	if x in factors_mem:
		return factors_mem[x]
	factors = []

	for i in range(1, min(int(sqrt(x)), upper_bound_factor) + 1):
		if x % i == 0:
			r = i
			c = x // i

			if r <= M and c <= N:
				factors.append((r, c))
			
			if c <= M and r <= N:
				factors.append((c, r))
	
	factors_mem[x] = factors
	return factors

def search(x): # x - number in grid
	factors = getFactors(x) # (r,c) - positions to jump to next 

	if (M, N) in factors:
		return "yes"
	else:
		for i in range(len(factors)):
			row, col = factors[i]

			# adjust so that we are in grid format
			row -= 1
			col -= 1

			if (row, col) in mem:
				continue
			else:
				# at this point we are not storing the result, we are just making sure we do not process a node we have already processed
				mem[(row, col)] = 0

			new_x = grid[row][col]
			result = search(new_x)
			
			if result == "yes":
				return "yes"

	return "no"
	
print(search(grid[0][0]))