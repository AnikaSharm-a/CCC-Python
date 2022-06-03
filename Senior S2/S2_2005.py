# CCC 2005 S2 https://www.cemc.uwaterloo.ca/contests/computing/2005/stage1/seniorEn.pdf


max_wh = list(map(int,input().split()))

groups = []
group = list(map(int,input().split()))
groups.append(group)

while group != [0,0]:
	group = list(map(int,input().split()))
	groups.append(group)

groups.remove(groups[-1])


currentpos = [0,0]

for pos in groups:
	x = currentpos[0] 
	y = currentpos[1] 
	
	x += pos[0]
	y += pos[1]

	if x > max_wh[0]: x = max_wh[0]
	elif x < 0: x = 0
	if y > max_wh[1]: y = max_wh[1]
	elif y < 0: y = 0
	
	currentpos = [x,y]

	print(x,y)