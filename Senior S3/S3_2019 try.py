# CCC 2019 S3 https://www.cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

grid = []

for i in range(3):
	temp = input().split()
	for i in range(3):
		if temp[i] != "X": temp[i] = int(temp[i])
	grid.append(temp)


# Checking rows for the x's: works if there is only one x per row horizontally
def checkrows(g):

	for r in g:
		if r[0] == "X":
			d = r[2] = r[1]
			r[0] = r[1] - d

		elif r[1] == "X":
			d = (r[2] - r[0]) / 2
			r[1] = int(r[0] + d)

		elif r[2] == "X":
			d = r[1] - r[0]
			r[2] = r[1] + d

	return g


newg = checkrows(grid)

print(newg[0][0], newg[0][1], newg[0][2])
print(newg[1][0], newg[1][1], newg[1][2])
print(newg[2][0], newg[2][1], newg[2][2])