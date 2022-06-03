# CCC 2019 J4/S1 https://cemc.uwaterloo.ca/contests/computing/2019/stage%201/seniorEF.pdf

# initial numbers and positions
TLnum = 1
TRnum = 2
BLnum = 3
BRnum = 4

def horizontalFlip():
  global TLnum, TRnum, BLnum, BRnum
  # left side horizontal flip
  temp = TLnum
  TLnum = BLnum
  BLnum = temp

  # right side horizontal flip
  temp2 = TRnum
  TRnum = BRnum
  BRnum = temp2
  
def verticalFlip():
  global TLnum, TRnum, BLnum, BRnum
  # top flip
  temp = TLnum
  TLnum = TRnum
  TRnum = temp

  # bottom flip
  temp2 = BLnum
  BLnum = BRnum
  BRnum = temp2

# imagine letters is a list - make input into a list
letters = list(input())

# perform flips 
for i in letters:
  if i == "H":
    horizontalFlip()
  else:
    verticalFlip()

# output
print(TLnum, TRnum)
print(BLnum, BRnum)