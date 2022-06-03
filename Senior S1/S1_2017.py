# CCC 2017 S1 https://www.cemc.uwaterloo.ca/contests/computing/2017/stage%201/seniorEF.pdf

n = int(input())
swifts = input().split(" ")
semaphores = input().split(" ")

sum_swifts = 0
sum_semaphores = 0
days = []

for i in range(n):
  sum_swifts += int(swifts[i])
  sum_semaphores += int(semaphores[i])

  if sum_swifts == sum_semaphores:
    days.append(i+1)

if len(days) == 0:
  final = 0
else:
  final = max(days)

print(final)