# CCC 2017 S2 https://cemc.uwaterloo.ca/contests/computing/2017/stage%201/seniorEF.pdf

n = int(input())
ms = input().split(" ") 
ms.sort(key = int)

lowtides = []

for x in ms[:round(n/2)]:
  lowtides.append(x)
  ms.remove(x)

lowtides.sort(key = int, reverse = True)

i = 1
j = 0

while len(lowtides) != n:
  lowtides.insert(i, ms[j])
  i += 2
  j += 1

for m in lowtides: 
  print(m, end = " ") 