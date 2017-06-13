
# try: 
# 	f = open('/home/vagrant/Downloads/test.txt', 'r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()


# with open('/home/vagrant/Downloads/test.txt', 'r') as f: # with语句会自动帮我们调用f.close()
# 	print(f.read())

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉

with open('/home/vagrant/Downloads/test.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip()) # 把末尾的'\n'删掉


with open('/home/vagrant/Downloads/test.txt', 'w') as f:
	f.write('hello, ian, flks, kaka!') # 会覆盖原来文件的内容