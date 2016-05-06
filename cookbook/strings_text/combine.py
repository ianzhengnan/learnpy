
def sample():
	yield 'Is'
	yield 'Chicago'
	yield 'Not'
	yield 'Chicago?'

text = ' '.join(sample())

print(text)


def combine(source, maxsize):
	parts = []
	size = 0

	for part in source:
		parts.append(part)
		size += len(part)
		if size > maxsize:
			# return to print
			yield ','.join(parts)
			parts = []
			size = 0
	# return to print
	yield ','.join(parts)

for part in combine(sample(), 10):
	# f.write(part)
	print(part)