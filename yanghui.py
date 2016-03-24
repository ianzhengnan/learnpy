
def yanghui(n):

	tl = []
	pl = []

	for i in range(n):
		if i == 0:
			tl.append(1)
			pl = tl
		else:
			pl = []

			for j in range(i + 1):
				if j - 1 == -1:
					pl.append(tl[j])
				elif j >= len(tl):
					pl.append(tl[j-1])
				else:
					pl.append(tl[j-1] + tl[j])

			tl = pl

		yield (pl)


def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]

def normalize(name):
    first = name[0:1]
    other = name[1:]

    return first.upper() + other.lower()

from functools import reduce

def prod(L):
	def mutiple(x, y):
		return x * y
	return reduce(mutiple, L)

def str2float(s):

	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}[s]

	def fn(x, y):
		if y == '.':
			return x
		else:
			return x * 10 + y


	n = 0
	n = s.find('.')

	if n != 0 and n != -1:
		n = len(s) - n - 1
		return reduce(fn, map(char2num, s)) / 10 ** n
	else:
		return reduce(fn, map(char2num, s))


def is_palindrome(n):

    st = str(n)
    ln = int(len(st) / 2)

    if ln == 0:
        return True
    else:
        ly = ''
        lx = [x for x in st[-ln:]]
        lx.reverse()
        for x in lx:
            ly = ly + x
        if  st[:ln] == ly:
            return True
        else:
            return False


def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

import functools

def log(text):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, (str, int, float)):
                print('%s %s():' % (text, func.__name__))
            else:
                print('Begin %s():' % func.__name__)
            result = func(*args, **kw)
            print('End %s():' % func.__name__)
            return result

        return wrapper

    if isinstance(text, (str, int, float)):
        return decorator
    else:
        return decorator(text)

# import mypython.hello
#
# mypython.hello.test()

# Run
#===========================================================================================

#@log('Ian')
@log
def now():
    print('2016-3-21')

now()


# L = [('Bob', 75), ('Adam', 92), ('Lisa', 88)]
# lx = sorted(L, key=by_score)
# print(lx)

# output = filter(is_palindrome, range(1, 10000))
# print(list(output))


# print(str2float('12.3456'))

# print(prod([3,2,1]))

# L1 = ['amanda', 'iAn', 'shELLy']
#
# L2 = list(map(normalize, L1))
#
# print(L2)

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break