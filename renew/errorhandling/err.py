import pdb

s = '0'
n = int(s)
pdb.set_trace() # 设置断点
print(10/n)

# $ python3 -m pdb err.py
# > /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
# -> s = '0'

# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

# (Pdb) l
#   1     # err.py
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)

# 输入命令n可以单步执行代码：

# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)

# 任何时候都可以输入命令p 变量名来查看变量：

# (Pdb) p s
# '0'
# (Pdb) p n
# 0

# 输入命令q结束调试，退出程序：

# (Pdb) q


# 程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

# $ python3 err.py 
# > /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
# -> print(10 / n)
# (Pdb) p n
# 0
# (Pdb) c
# Traceback (most recent call last):
#   File "err.py", line 7, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero


