
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。


from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue()) # 'hello world'


fl = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = fl.readline()
	if s == '':
		break
	print(s.strip())

from io import BytesIO

fb = BytesIO()
fb.write('中文'.encode('utf-8'))
print(fb.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'


