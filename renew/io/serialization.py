
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

import pickle

d = dict(name='Bob', age=20, score=99)
print(pickle.dumps(d)) # b'\x80\x03}q\x00(X\x05\x00\x00\x00scoreq\x01KcX\x03\x00\x00\x00ageq\x02K\x14X\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

# >>> f = open('dump.txt', 'wb')
# >>> pickle.dump(d, f)
# >>> f.close()

# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

# >>> f = open('dump.txt', 'rb')
# >>> d = pickle.load(f)
# >>> f.close()
# >>> d
# {'age': 20, 'score': 88, 'name': 'Bob'}

import json

print(json.dumps(d))  # {"score": 99, "age": 20, "name": "Bob"}

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Bob', 20, 98)
print(json.dumps(s, default=student2dict))  # 转换函数，告诉json怎么序列化这个对象  {"score": 98, "age": 20, "name": "Bob"}

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))  # <__main__.Student object at 0x7f679d6e55f8>
