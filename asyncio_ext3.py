
import threading
import asyncio

@asyncio.coroutine
def print_sum(x, y):
    result = yield from compute(x,y)
    print('%s + %s = %s' % (x, y, result))


@asyncio.coroutine
def compute(x, y):
    print('Compute %s + %s' % (x, y))
    yield from asyncio.sleep(3)
    return x + y

@asyncio.coroutine
def comput2(x, y):
    print('Compute2 for %s + %s = %s' % (x, y, (x + y)))


loop = asyncio.get_event_loop()
# only the functions in this list will be saw as async, understand!!!
# if there is only one function, it is sync
tasks = [print_sum(1, 2), comput2(2,3)]
# loop.run_until_complete(print_sum(1,2)) # execute for 1 function
loop.run_until_complete(asyncio.wait(tasks)) # execute for a function list
loop.close()