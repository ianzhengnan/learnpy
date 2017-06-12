
class Student(object):

	def __init__(self, name):
		self.name = name


	def __str__(self):
		return 'Student object (name is %s)' % self.name

	__repr__ = __str__ # __repr__是给程序员调试用的

	def __call__(self):
		print('My name is %s' % self.name)


s = Student('Michael')
print(s) # Student object (name is Michael)
s() # 因为有__call__ 所以可以当函数调用
print(callable(s)) # 判断一个对象是否可以调用callable(object)

class Fib():
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):  # 返回一个迭代器对象
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a 


fib = Fib()
print(fib)

for n in Fib():
	print(n)

print(fib[0])
print(fib[2])
print(fib[3])
print(fib[4])


class Chain():
	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__


print(Chain().status.user.timeline.list)
