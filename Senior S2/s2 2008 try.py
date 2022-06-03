# CCC 2008 S2 https://www.cemc.uwaterloo.ca/contests/computing/2008/stage1/seniorEn.pdf

# works but needs to be optimized for last two cases


radius = int(input())
radii = []  
radii.append(radius)

while radius > 0:
	radius = int(input())
	radii.append(radius)

radii.remove(radii[-1])

totals = []


def getfirstnum(r):
	quad1num = 0

	for i in range(r+1):
		for j in range(r+1):
			if i**2 + j**2 <= r**2: quad1num += 1

	return quad1num


for radius in radii:
	quad1num = getfirstnum(radius)
	quad2num = quad1num - (radius + 1)
	quad4num = quad1num - ((2*radius) + 1)

	total = quad1num + 2*quad2num + quad4num
	totals.append(total)


for total in totals:
	print(total)