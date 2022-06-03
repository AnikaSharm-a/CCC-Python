# CCC 2020 S3 https://www.cemc.uwaterloo.ca/contests/computing/2020/ccc/seniorEF.pdf

needle = input()
haystack = input()

if len(needle) > len(haystack): print(0)
else:

	# creating needle map
	needle_map = {}
	for c in "abcdefghijklmnopqrstuvwxyz":
		needle_map[c] = 0
	for c in needle:
		needle_map[c] += 1

	seen_needles = {}
	total = 0

	# initializing haystack map
	haystack_map = {}
	for c in "abcdefghijklmnopqrstuvwxyz":
		haystack_map[c] = 0
	for i in range(len(needle)):
		c = haystack[i]
		haystack_map[c] += 1

	# checking for first group
	if haystack_map == needle_map:
		key = haystack[:len(needle)]
		
		if key not in seen_needles:
			seen_needles[key] = 1
			total += 1

	# checking for rest of the groups
	for i in range(1, len(haystack) - len(needle) + 1):

		haystack_map[haystack[i - 1]] -= 1
		haystack_map[haystack[i + len(needle) - 1]] += 1

		if haystack_map == needle_map:
			key = haystack[i : i + len(needle)]
			if key not in seen_needles:
				seen_needles[key] = 1
				total += 1

	print(total)