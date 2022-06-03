# CCC 2010 S1 https://www.cemc.uwaterloo.ca/contests/computing/2010/stage1/seniorEn.pdf

def parseinput(n):
	global data
	data = []
	for i in range(n):
		line = input().split()
		name = line[0]
		R = int(line[1])
		S = int(line[2])
		D = int(line[3])
		formula = (2*R) + (3*S) + D
		data.append([formula,name])
	data.sort(reverse = True)


numc = int(input())

if numc == 0: pass
elif numc == 1: print(input().split()[0])


elif numc == 2: 
	parseinput(numc)
	answer1 = data[0][1]
	answer2 = data[1][1]

	if data[0][0] == data[1][0]:
		if data[0][1] > data[1][1]: 
			answer1 = data[1][1]
			answer2 = data[0][1]

	print(answer1)
	print(answer2)


else:
	parseinput(numc)

	answer1 = data[0][1]
	answer2 = data[1][1]

	if data[0][0] == data[1][0]:
		if data[1][1] < data[0][1]: 
			answer1 = data[1][1]
			answer2 = data[0][1]

	if data[1][0] == data[2][0]:
		if data[2][1] < data[1][1]: 
			answer2 = data[2][1]

	print(answer1)
	print(answer2)