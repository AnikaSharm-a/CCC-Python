# CCC 2016 S2: https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/seniorEn.pdf

typeQ = input()
n = int(input())

line1 = [int(x) for x in input().split(" ")]
line1.sort()

line2 = [int(y) for y in input().split(" ")]
line2.sort()

minSum = 0
for i in range(n):
  minSum += max(line1[i],line2[i])

maxSum = 0
for i in range(n):
  maxSum += max(line1[i],line2[n-i-1])

if typeQ == "1":
  print(minSum)
elif typeQ == "2":
  print(maxSum)