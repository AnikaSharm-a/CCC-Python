# CCC 2011 S2 https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

n = int(input())

student = [input() for i in range(n)]
correct = [input() for i in range(n)]
qs = 0

for i in range(n):
	if student[i] == correct[i]: qs += 1

print(qs)