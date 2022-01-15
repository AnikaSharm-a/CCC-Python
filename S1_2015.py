# CCC S1 2015 https://cemc.uwaterloo.ca/contests/computing/2015/stage%201/seniorEn.pdf


# cw's code (without an array):


# Hints to not use an array:
# - Order doesn't matter (to a degree)
# Hints specific to this problem:
# --> We are only ever mutating the end of the array
# --> When we process the array, order is irrelevant to us

k = int(input())

total = 0
last_num = 0

for i in range(k):
    n = int(input())

    if n == 0:
        total -= last_num
    else:
        total += n
        last_num = n


# cw's code (with 1 array):


k = int(input())

nums = []
for i in range(k):
    n = int(input())

    if n == 0 and len(nums) > 0:
        nums.pop(-1)
    else:
        nums.append(n)

total = sum(nums)

print(total)

# --------------------

k = int(input())
nums = []

# taking the sequence of numbers and storing it in a list 
for i in range(k):
  num = int(input())
  nums.append(num)

nums2 = []

# append all numbers that need to be calculated for sum in a new list
for j in nums:
  nums2.append(j)
  if j == 0:
    nums2.remove(nums2[-1]) # remove zero
    nums2.remove(nums2[-1]) # remove number before zero

total = 0

# do the sum
for k in nums2:
  if len(nums2) == 0: 
    total = 0 
  else: 
    total += k

print(total)