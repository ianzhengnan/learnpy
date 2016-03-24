
class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


    def run(self):
        print('Student is running...')

dog = Dog()
cat = Cat()

run_twice(Student('Ian', 100))
