# CCC 2022

# # S1
# n = int(input())
# max5s = n//5
# max4s = n//4
# count = 0

# for i in range(max5s+1):
# 	if (n-i*5) % 4 == 0: count += 1

# print(count)





# S2

# x = int(input())
# mustbetogether = [input().split() for i in range(x)]

# y = int(input())
# nottogether = [input().split() for i in range(y)]

# g = int(input())
# groups = [input().split() for i in range(g)]

# violations = 0




# for i in range(x):

# 	p1 = mustbetogether[i][0]
# 	p2 = mustbetogether[i][1]

# 	for group in groups:

# 		if (p1 in group and p2 not in group) or (p2 in group and p1 not in group): 
# 				violations += 1
# 				break



# for i in range(y):

# 	p1 = nottogether[i][0]
# 	p2 = nottogether[i][1]

# 	for group in groups:

# 		if p1 in group and p2 in group: 
# 				violations += 1
# 				break



# print(violations)






# S3

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# from itertools import permutations

# thing = input().split()

# N = int(thing[0])
# M = int(thing[1])
# K = int(thing[2])

# all_pieces = []
# def recur(x, l):
#     if x == N:
#         all_pieces.append(l[:])
#     else:
#         for m in range(1, M + 1):
#             l.append(m)
#             recur(x + 1, l)
#             l.pop()


# recur(0, [])    

# #all_pieces = list(permutations(range(1, M + 1), N, repeat=True))
# for piece in all_pieces:
#     count_of_good_samples = 0
#     # Going through all possible samples
#     for n1 in range(len(piece)):
#         for n2 in range(n1, len(piece)):
           
#             if len(set(piece[n1:n2 + 1])) == (n2 - n1 + 1):
#                 count_of_good_samples += 1
#     if count_of_good_samples == K:
#         print(*piece)
#         exit()
#     print("\n")
# print("-1")