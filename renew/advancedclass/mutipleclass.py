
class Animal(object):
	pass

class FlyableMixIn(object):
	pass

class RunableMixIn(object):
	pass

class Dog(Animal, RunableMixIn):
	pass

class Bird(Animal, FlyableMixIn):
	pass

