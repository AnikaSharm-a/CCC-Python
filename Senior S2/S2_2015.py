# CCC 2015 S2 https://www.cemc.uwaterloo.ca/contests/computing/2015/stage%201/seniorEn.pdf

# Taking all input
numJerseys = int(input())
numAthletes = int(input())
jerseySizes = [input() for i in range(numJerseys)]
requests = [input().split() for i in range(numAthletes)]
satisfied = 0

for i in range(numAthletes):
	jerseyIndex = int(requests[i][1]) - 1
	
	if jerseySizes[jerseyIndex] == requests[i][0]: 
		satisfied += 1
		jerseySizes[jerseyIndex] = "T"
	
	else:
		if jerseySizes[jerseyIndex] == "T": continue
		else:
			if jerseySizes[jerseyIndex] == "S": rank1 = 1
			elif jerseySizes[jerseyIndex] == "M": rank1 = 2
			else: rank1 = 3

			if requests[i][0] == "S": rank2 = 1
			elif requests[i][0] == "M": rank2 = 2
			else: rank2 = 3

			if rank1 > rank2: 
				satisfied += 1
				jerseySizes[jerseyIndex] = "T"

print(satisfied)