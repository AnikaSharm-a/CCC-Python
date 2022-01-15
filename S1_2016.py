# CCC 2016 S1 https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/seniorEn.pdf

# things for the future:
# - thinking of test cases
# - walking through code in your head

# ==> Your challenge: What is that case?:
# Any case where the strings have a different number of the same characters- total number of characters is also the same
# for example: string 1= abcdabcd, string 2= aaadabcd --> 1 has 2 a's and 2 has 4 a's, however, the program will output "A"

# the program will stop looking after a match has been made, however, it does not eliminate the character after being found in the first string, thus making it so that each character is matched every time it checks for a match
# to fix this, you must remove the character from the first string after matched

# ==> QUESTIONS:
# Can this idea can be implemented without turning the strings into lists?- if yes, how?
# You can modify strings by concatenating them like "a"+"b" = "ab"
# You can use replace() but it is a lot easier and faster to turn them into lists

#https://www.hackerrank.com/challenges/plus-minus/problem 
# how to make it so that round() does not omit 0s at the end of the number- eg. print 9.230000 instead of 9.23 
# print("%.6" % (9.23))

first = list(input())
second = list(input())

checker = 0

# check for any asterisks
for c in second:
  if c == "*":
    checker += 1

# check each character individually to find match
for c in second:
  for i in first:
    if c != "*" and c == i:
      checker += 1
      first.remove(i) 
      break

# output
if checker == len(first):
  print("A")
else:
  print("N")