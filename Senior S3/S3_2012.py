# CCC 2012 S3 https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

sensors = int(input())

def checkifdoubles(count):
	freq = count[0][0]
	for i in range(1, len(count)):
		if count[i][0] == freq: return True
	return False

if sensors == 2:
	r1 = int(input())
	r2 = int(input())
	print(abs(r1-r2))

else:
	readings = [int(input()) for i in range(sensors)]
	count = {}

	for num in readings:
		count[num] = 0
	for num in readings:
		count[num] += 1 

	count = list(count.items())
	count = [list(x) for x in count]

	for i in range(len(count)):
		count[i][0], count[i][1] = count[i][1], count[i][0]

	count.sort(reverse = True)
	

	if checkifdoubles(count):
		r1 = count[0][1]
		r2 = count[1][1]
		freq = count[0][0]

		for i in range(len(count)):
			if count[i][0] == freq:
				if count[i][1] > r1: r1 = count[i][1]
				if count[i][1] < r2: r2 = count[i][1]

		print(abs(r1-r2))

	else:
		r1 = count[0][1]
		freq = count[1][0]

		temp = []

		for i in range(1, len(count)):
			if count[i][0] == freq: temp.append(count[i])

		diff = abs(r1 - temp[0][1])
		for i in range(1, len(temp)):
			diff2 = abs(r1 - temp[i][1])
			if diff2 > diff: diff = diff2

		print(diff)