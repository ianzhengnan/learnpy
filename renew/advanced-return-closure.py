
def lazy_sum(*args):
	def sum():
		result = 0
		for i in args:
			result += i
		return result
	return sum

f1 = lazy_sum(1,2,3,4)
print(f1()) # 真正计算在这里


# closure 闭包

def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	return fs

def count2():
	def f(j):
		return lambda : j * j # 通过lambda简化
	fs = []
	for i in range(1, 4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	return fs

f1, f2, f3 = count2()
print(f1(), f2(), f3())

