#Things to talk about: 
  #Recursions
  #Trees

# CCC 2018 J4/S2 https://cemc.uwaterloo.ca/contests/computing/2018/stage%201/seniorEF.pdf

n = int(input())
flowers = []

for i in range(n):
  flower = list(map(int, input().split(" ")))
  flowers.append(flower)
 
shortest = flowers[0][0] # top left corner

# top right corner
if flowers[0][n-1] < shortest:
  shortest = flowers[0][n-1]

# bottom left corner
if flowers[n-1][0] < shortest:
  shortest = flowers[n-1][0]

# bottom right corner
if flowers[n-1][n-1] < shortest:
  shortest = flowers[n-1][n-1]

x = 2
y = 2

# printing 360 degree rotation
if shortest == flowers[0][0]:
  for i in flowers:
    for j in i:
      print(j, end = " ")
    print("")

# printing 90CW or 270CCW degree rotation
elif shortest == flowers[0][n-1]:
  for i in range(n):
    for j in range(n):
      print(flowers[j][x], end = " ")
    x -= 1
    print("")

# printing 180 degree rotation
elif shortest == flowers[n-1][n-1]:
  for i in range(n):
    x = 2
    for j in range(n):
      print(flowers[y][x], end = " ")
      x -= 1
    print("")
    y -= 1

# printing 270CW or 90CCW degree rotation
elif shortest == flowers[n-1][0]:
  for i in range(n):
    x = 2
    for j in range(n):
      print(flowers[x][i], end = " ")
      x -= 1
    print("")