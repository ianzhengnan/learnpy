
class student(object):
	"""docstring for student"""
	def __init__(self, name, score):
		# super(student, self).__init__()
		self.__name = name   # 私有化了，在外部变成_Student__name
		self.__score = score
		
	def get_name(self):
		return self.__name

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))



if __name__ == '__main__':
	
	std1 = student('ian', 35)
	std2 = student('kaka', 23)

	std1.print_score()

	std1.__name = 'test' # 这里的__name不是类里的__name. 是python动态给对象添加的新属性～～～～～

	print(std1.__name) # test
	print(std1.get_name())  # ian
