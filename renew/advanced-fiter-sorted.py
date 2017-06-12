
# filter返回一个迭代器（也是生成器）
# 传入的函数必须返回一个布尔值

def is_odd(n):
	return n % 2 == 0

l1 = list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10]))

print(l1)

def not_empty(s):
	return s and s.strip()

l2 = list(filter(not_empty, ['', '   ', None, 'test', '3', '     ']))

print(l2)

print(sorted([-32, -3,2,56,23]))
print(sorted([-32, -3,2,56,23], key = abs)) # 通过KEY传入一个函数进行自定义排序， 对abs的返回结果进行排序

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))



