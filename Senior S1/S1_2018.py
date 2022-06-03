# CCC 2018 S1 https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf
# next time talk about: debugging

"""
===Talking about debugging===

Things you can do:
 - print values
 - try to work through the program in your head (or out loud)
 - Isolating parts of the program & isolating the problem

def a():


def b():


def c():
    b() + a()


def main():
    for i in range(10):
        print(c())


"""


# first input 
numV = int(input())

villages = []

# rest of the inputs
for i in range(0,numV):
  village = int(input())
  villages.append(village)

villages.sort()

sizes = []

# figure out the sizes of each village
for i in range(1,len(villages)-1):
  a = villages[i-1]
  b = villages[i]
  c = villages[i+1]
  
  size = ((b-a)/2) + ((c-b)/2)
  sizes.append(size)

sizes.sort()
print(sizes[0])