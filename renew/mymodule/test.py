 
' test '

__author__ = 'Ian Zheng'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')


if __name__ == '__main__':
	print('test')
	test() # 额外的代码，只在命令行运行此文件的时候会执行