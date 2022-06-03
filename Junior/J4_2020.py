# j4 2020 

text = input()
string = input()

string = list(string)
shifts = []

for i in range(len(string)):
	char = string[0]
	string.remove(char)
	string.append(char)
	newstr = ""
	for i in string:
		newstr += i
	shifts.append(newstr)

found = False

if len(text) < len(string): print("no")
else:
	
	for i in range(len(text)):
		part = text[i:len(string)+i]
		
		if part in shifts: 
			found = True
			break

	if found: print("yes")
	else: print("no")