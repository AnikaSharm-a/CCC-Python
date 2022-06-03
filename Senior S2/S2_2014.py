# CCC 2014 S2 https://www.cemc.uwaterloo.ca/contests/computing/2014/stage%201/seniorEn.pdf

n = int(input()) # num students
line1 = input().split()
line2 = input().split()

d = {}
out = "good"

for i in range(n):
	d[line1[i]] = line2[i]

for key in d:
	val = d[key] 
	val1 = d[val] 
	if val1 != key:
		out = "bad"
		break

for i in range(n):
    if line1[i] == line2[i]: 
        out = "bad"
        break

print(out)