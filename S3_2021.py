# CCC 2021 S3 https://www.cemc.uwaterloo.ca/contests/computing/2021/ccc/seniorEF.pdf

# Solving simpler problems
# - Ignore the walking speed ==> Look for the intersections
# - Solve for just 1 person

n = int(input()) # num friends
data = []
for i in range(n):
	data.append(list(map(int, input().split())))

max_pos = 0
for v in data:
	if v[0] > max_pos:
		max_pos = v[0]
#numberline = [0 for i in range(1000000)]
numberline = [0 for i in range(max_pos)]
# ^ football field
for i in range(n):
	position = data[i][0]
	speed = data[i][1]
	hearingd = data[i][2]
		
	# hearing_range + 1 is when we need to start adding
	for diff in range(1, len(numberline)):
		left_x = position - diff - (hearingd)
		right_x = position + diff + (hearingd)
	
		# add (diff * duration (W))
		if left_x >= 0:
			numberline[left_x] += diff*speed 
		if right_x < len(numberline):
			numberline[right_x] += diff*speed

		# once both coordinates are out of bounds,
		# stop looping
		if left_x < 0 and right_x >= len(numberline):
				break

	#print(numberline)

		
print(min(numberline))