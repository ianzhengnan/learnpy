
with open("test.txt") as f:
	# this is a generator iterator
	lines = (line.strip() for line in f)
	for line in lines:
		print(line)


