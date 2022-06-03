# CCC 2011 S1 https://www.cemc.uwaterloo.ca/contests/computing/2011/stage1/seniorEn.pdf

n = int(input())
string = ""

for i in range(n):
	string += input()


def tChars(letters):
	tcount = 0
	for char in letters:
		if char == "t" or char == "T": tcount += 1
	return tcount


def sChars(letters):
	scount = 0
	for char in letters:
		if char == "s" or char == "S": scount += 1
	return scount


t = tChars(string)
s = sChars(string)

if t>s: print("English")
elif s>t: print("French")
elif s==t: print("French")