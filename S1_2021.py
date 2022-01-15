# CCC 2021 S1 https://www.cemc.uwaterloo.ca/contests/computing/2021/ccc/seniorEF.pdf

numWoods = int(input())
lengths = input().split(" ")
widths = input().split(" ")
totalArea = 0

for i in range(numWoods):
  b1 = int(lengths[i])
  b2 = int(lengths[i+1])
  h = int(widths[i])

  totalArea += ((b1+b2)*h)/2 

if (totalArea * 10) % 10 == 5:
  # print normally, because there is a .5
  print(totalArea)
else:
  print(int(totalArea))