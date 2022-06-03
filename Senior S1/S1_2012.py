# CCC 2012 S1 https://www.cemc.uwaterloo.ca/contests/computing/2012/stage1/seniorEn.pdf

n = int(input())

total = 0

for i in range(1, n):
  for j in range(1, i):
    for k in range(1, j):
      # by the way we set this loop up, we know that:
      # k < j, j < i, i < n
      total += 1

print(total)