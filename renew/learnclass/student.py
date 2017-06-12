
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self): # 这里如果不给出self参数会报错说定义了0个参数，却给了一个参数
		print("%s's score is %d" % (self.name, self.score))



if __name__ == '__main__':
	stud1 = Student('xiaowang', 88)
	stud2 = Student('ian', 98)

	stud1.print_score()
	stud2.print_score()

	print(stud2.name)
	stud2.name = 'kaka'
	print(stud2.name)
	print(stud2.__str__())
	Student.print_score(stud2) # kaka's score is 98
	
