
import os

print(os.name) # posix

print(os.uname()) #posix.uname_result(sysname='Linux', nodename='vagrant', release='3.19.0-25-generic', version='#26~14.04.1-Ubuntu SMP Fri Jul 24 21:16:20 UTC 2015', machine='x86_64')

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

print(os.environ) # 显示系统所有环境变量
print('--------------------------------------------------------------------')
print(os.environ.get('PATH'))

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# # 查看当前目录的绝对路径:
# >>> os.path.abspath('.')
# '/Users/michael'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')

# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')

# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')

# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

# >>> [x for x in os.listdir('.') if os.path.isdir(x)]
# ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]

# 要列出所有的.py文件，也只需一行代码：

# >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

# 是不是非常简洁？