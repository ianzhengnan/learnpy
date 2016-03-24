

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n,int):
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop

            if start is None:
                start = 0

            L = []

            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Chain(object):
    def __init__(self, path=''):
        self._path = path;

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self, *args, **kwargs):
        return Chain('%s/:%s' % (self._path, args[0]))


#test---------------------------------------------------------------------------------------------------------

print(Chain().users('Micheal').repos)


# s = Screen()
#
# s.width = 1024
# s.height = 768
#
# print(s.resolution)
#
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# for n in Fib():
#     print(n)

# f = Fib()
#
# print(f[0:5])
#
# print(f[:10])

