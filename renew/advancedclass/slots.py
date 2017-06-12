

class Student(object):
	pass



s = Student()
s.name = 'kaka' # 动态添加的属性

from types import MethodType

def set_age(self, age):
	self.age = age

s.set_age = MethodType(set_age, s)

s.set_age(25)

print(s.age, s.name)

# 给所有的实例绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s2 = Student()
s2.set_score(99)
print(s2.score)

s.set_score(98)
print(s.score)


class Animal(object):
	__slots__ = ('price', 'weight') # 限定Animal只能有price， weight两个属性

a = Animal()
a.price = 23
a.weight = 2
# a.name = 'kaka' # 加不了了

class Dog(Animal):
	pass

dog = Dog()

# dog.name = 'kaka' # 子类一样加不了
dog.price = 22 # 可以添加