
class Student(object):

	@property # 生成一个getter
	def birth(self):
		return self._birth

	@birth.setter # 由@property 生成的一个装饰器，用来修饰一个setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):   # age 是只读属性
		return 2017 - self._birth

	# @age.setter
	# def age(self,value):
	# 	self._age = value


s = Student()

s.birth = 1982
print(s.birth)
print(s.age)
# s.age = 23 # 会报错


