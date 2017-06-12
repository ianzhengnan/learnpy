
def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		yield b
		a, b = b, a + b
		n += 1

	print('done')

for i in fib(20):
	print(i)

