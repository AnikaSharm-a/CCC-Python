# CCC 2019 junior contest



# j1 
# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# at = 3*a1 + 2*a2 + a3

# b1 = int(input())
# b2 = int(input())
# b3 = int(input())
# bt = 3*b1 + 2*b2 + b3

# if at > bt: print("A")
# elif bt > at: print("B")
# else: print("T")




# j2
# n = int(input())
# sols = []
# for i in range(n):
# 	m = input().split()
# 	m[0] = int(m[0])
# 	sols.append(m[0]*m[1])
# for item in sols:
# 	print(item)





# j3
# n = int(input())
# num = 0

# sol1 = []
# sol2 = []

# for i in range(n):
# 	string = input()


# 	for i in range(len(string)):
		
# 		if i == len(string)-1:
			
# 			if string[i] == string[i-1]:
# 				num += 1
# 				char = string[i]
# 				sol1.append([num,char])

# 			else:
# 				num = 1
# 				char = string[i]
# 				sol1.append([num,char])


# 		else:
			
# 			if string[i] == string[i+1]:
# 				num += 1
# 				char = string[i]


# 			else:
# 				num += 1 
# 				char = string[i]
# 				sol1.append([num,char])
# 				num = 0


# 	a = ""
# 	for group in sol1:
# 		a += str(group[0]) + " " + group[1] + " "
# 	sol2.append(a)
# 	sol1 = []
# 	num = 0

# for i in sol2:
# 	print(i)





# # J4
# # initial numbers and positions
# TLnum = 1
# TRnum = 2
# BLnum = 3
# BRnum = 4

# def horizontalFlip():
#   global TLnum, TRnum, BLnum, BRnum
#   # left side horizontal flip
#   temp = TLnum
#   TLnum = BLnum
#   BLnum = temp

#   # right side horizontal flip
#   temp2 = TRnum
#   TRnum = BRnum
#   BRnum = temp2
  
# def verticalFlip():
#   global TLnum, TRnum, BLnum, BRnum
#   # top flip
#   temp = TLnum
#   TLnum = TRnum
#   TRnum = temp

#   # bottom flip
#   temp2 = BLnum
#   BLnum = BRnum
#   BRnum = temp2

# # imagine letters is a list - make input into a list
# letters = list(input())

# # perform flips 
# for i in letters:
#   if i == "H":
#     horizontalFlip()
#   else:
#     verticalFlip()

# # output
# print(TLnum, TRnum)
# print(BLnum, BRnum)




# J5- dont know