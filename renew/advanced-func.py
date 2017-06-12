# 可以传入意外一个函数的函数为高阶函数, map(), reduce()就是这样的函数，他们都可以接收一个函数作为参数

def abs_add(x, y, f):
	return f(x) + f(y)

print(abs_add(-12, 23, abs))

def f(x):  # f 只能接受一个参数
	return x * x

r = map(f, [1,2,3,4,5,6]) # map返回一个迭代器（也是生成器）

l1 = list(r) # 可以用过这种方式把迭代器变成一个list,tuple, 也可以直接用for循环这个迭代器(这种方式更好，懒加载的方式)

print(l1)

print(list(map(str,[1,2,3,4,5,6,7,8,9]))) # 将一个数字list转化为字符串list

from functools import reduce

def add(x, y): # add必须接受两个参数
	return x + y

print(reduce(add, [1,2,3,4,5])) # reduce就是把函数add计算的结果跟list下一个元素再运行add
# 上面这句相当于下面, sum是python的内置函数
print(sum([1,2,3,4,5]))

# 以下语句会报错，因为test要被reduce塞俩参数，而它只定义了一个
# def test(x):
# 	return x

# print(reduce(test, [1,2,3,4,5]))


# 练习：

#1
def normalize(name):
	return name[0].upper() + name[1:].lower()

print(list(map(normalize, ['adAm', 'lISa', 'iAn'])))

#2
def prod(l):
	return reduce(lambda x, y: x * y, l)

print(prod([1,2,3]))

# lambda返回一个函数，可以直接赋值给变量，然后通过变量调用此函数
# f = lambda x, y: x + y 

# <function <lambda> at 0x7fa5ab8e2950>
# >>> f(1,2)

#3
def str2float(s):

	# check pointer count
	if s.count('.') > 1:
		raise ValueError('invalid value: %s' % s) 

	# get pointer
	position = s.find('.')
	# s = s[:position] + s[position + 1:] 
	s = s.replace('.', '')

	def str2num(char):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[char]

	def calc(x, y):
		return x * 10 + y

	result = reduce(calc, map(str2num, s)) / 10 ** (len(s) - position)

	return result

print(str2float('123.4'))


