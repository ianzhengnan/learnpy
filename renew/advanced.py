
def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		yield b
		a, b = b, a + b
		n += 1

	print('done')

for i in fib(6):
	print(i)

def test(name, age, *args,  city, country):
	print(name, age, args, city, country)

test('kaka', 23, 45, city='test', country = 'China')

def f1(a, b, c = 0, *args, **kw):
	print('a = ',a, 'b = ',b, 'c = ',c,'args = ',args,'kw = ',kw)

def f2(a, b, c = 0, * , d, **kw):
	print('a = ',a,'b = ',b,'c = ',c,'d = ',d,'kw = ',kw)

f1(1,2)
f1(1,2,3,4,5, city='shanghai', country='China')
f2(1,2,4,d='kaka') # 命名关键字参数d， 必须要赋值
f2(1,2,3,d='kaka', city='shanghai', country='China')

it = iter([1,2,3,4,5]) # 快速生成一个迭代器。 所有的生成器都是迭代器，但是list, tuple, str不是迭代器，他们只是可迭代对象
for i in it:
	print(i)

