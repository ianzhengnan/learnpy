import os

print('process (%s) start...' % os.getpid())

pid = os.fork()  # fork 子进程永远返回0，而父进程返回子进程的ID。

if pid == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？

# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# 执行结果如下：

# Parent process 928.
# Process will start.
# Run child process test (929)...
# Process end.


