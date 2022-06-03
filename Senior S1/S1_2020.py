# CCC 2020 S1 S1https://cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf

n = int(input())
ms = []

for i in range(n):
  item = list(map(int, input().split(" "))) 
  ms.append(item)

ms.sort()
maxspeed = -1

for j in range(1,len(ms)):
  maint = ms[j][0]
  maind = ms[j][1]
  
  othert = ms[j-1][0]
  otherd = ms[j-1][1]

  timedif = abs(maint-othert)
  disdif = abs(maind-otherd)
  speed = disdif/timedif
  
  if speed > maxspeed:
    maxspeed = speed

print(round(maxspeed, 1))