
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

import functools

int2 = functools.partial(int, base=2)

int2('1000000') # 64
int2('1000010') # 65

max2 = functools.partial(max, 10)
max2(5,6,7) # 10 相当于调用了max(10, 5, 6 ,7) max(*arg)




