# CCC 2019 S2 https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

from math import sqrt

# this version of primechecker will get you the first 6 marks (woo!!)

# def primechecker(n):
#   if n == 1:
#     return False
#   for x in range(2,n):
#     if n % x == 0:
#       return False
#   return True

# this version will work up to 1 000 000 (full marks)
def primechecker(n):
  if n == 1:
    return False
  for x in range(2,int(sqrt(n) + 1)):
    if n % x == 0:
      return False
  return True

nums = int(input())
numbers = [] 

for i in range(nums):
  num = int(input())
  numbers.append(num)

for j in numbers:
  j *= 2
  for i in range(j):
    A = j-i
    B = j-A
    if primechecker(A) == True and primechecker(B) == True:
      print(A, B)
      break