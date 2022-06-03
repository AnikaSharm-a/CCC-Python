# CCC S2 2021 

m = int(input())
n = int(input())

s = int(input())
grid = []
gcount = 0

for i in range(m):
	grid.append(["B" for j in range(n)])	

moves = {}

for i in range(s):
	move = input()
	
	if move in moves: 
		moves[move] += 1
		if moves[move] == 2: moves.pop(move)
	
	else: moves[move] = 1

moves = list(moves)


for i in range(len(moves)):
	stroke = moves[i].split()
	
	if stroke[0] == "R":
		row = int(stroke[1])-1
		group = grid[row]

		for i in range(n):

			if group[i] == "B": 
				group[i] = "G"
				gcount += 1

			else: 
				group[i] = "B"
				gcount -= 1

	else:
		col = int(stroke[1])-1

		for group in grid:
			
			if group[col] == "B": 
				group[col] = "G"
				gcount += 1
			
			else: 
				group[col] = "B"
				gcount -= 1 

print(gcount)