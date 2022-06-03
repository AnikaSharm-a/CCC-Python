# CCC 2008 S1 https://www.cemc.uwaterloo.ca/contests/computing/2008/stage1/seniorEn.pdf

cities = []

group = input().split()
group[1] = int(group[1])
cities.append(group)

while True:
	group = input().split()
	group[1] = int(group[1])
	cities.append(group)

	if group[0] == "Waterloo" or group[0] == "waterloo": break

for i in range(len(cities)):
	cities[i][0], cities[i][1] = cities[i][1], cities[i][0]

cities.sort()
print(cities[0][1])