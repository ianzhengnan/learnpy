
# 想修改一个函数，给它增加功能，又不想更改它的定义，
# 这种在代码运行期间动态增加功能的方式叫做‘装饰器’

import functools

# 比如给函数加日志功能
def log(func):
	@functools.wraps(func)  # 如果不加这句，则now的__name__会被改成‘wrapper'
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)  # 装饰的内容
		return func(*args, **kw)
	return wrapper

@log
def now(date):
	print(date)


now('2017-6-12') # 实际执行的是 now = log(now) 
print(now.__name__)

# 如果要加参数

def logger(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))  # 装饰的内容
			return func(*args, **kw)
		return wrapper
	return decorator

@logger('execute')
def get_now(date): 
	print(date)

get_now('2017-6-12') # get_now = logger('execute')(get_now)
print(get_now.__name__)