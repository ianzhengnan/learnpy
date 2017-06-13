
# 运行时创建类和对象，可以用type()函数
# 因为动态语言是解释执行的，所以允许我们可以动态创建类和对象

def fn(self, name = 'world'):
	print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello类, 实际上，python的解释器也是这么创建类的

h = Hello()
h.hello()
print(type(Hello)) # <class 'type'>
print(type(h))  # <class '__main__.Hello'>


# metaclass, 先创建metaclass， 再通过它创建类。 就跟先创建类，根据类创建对象一样
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs) # 调用super的__new__方法，但这时attrs已经被增强

class MyList(list, metaclass = ListMetaclass):
	pass


l = MyList()
l.add(1) # add方法可以使用了
l.add(2)
l.add(3)
print(l) # [1,2,3]

# 这里正常做法可以直接在MyList里添加add方法，但是metaclass可以用在像ORM，表里的一条记录对应一个python对象

# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：

# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')

# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()

# 实现上面这个ORM
# -------------------------------------------------------------------------------
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys(): # 类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
			attrs.pop(k)

		attrs['__mappings__'] = mappings # 保存属性和列的对应关系
		attrs['__table__'] = name # 假设类名就是表名

		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))

		sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))


class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')


u = User(id=123, name='kaka', email='kaka@test.com', password='1234567')
u.save()

