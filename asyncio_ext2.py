import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(5)
    print('Hello again! (%s)' % threading.current_thread())

@asyncio.coroutine
def hi():
    print('Hi! (%s)' % threading.current_thread())
    yield from asyncio.sleep(6)
    print('Hi! again (%s)' % threading.current_thread())

@asyncio.coroutine
def pf(s):
    print(s)

loop = asyncio.get_event_loop()
tasks = [hello(), hi(), pf('1'), pf('2')]
# wait for all tasks done
loop.run_until_complete(asyncio.wait(tasks))
# execute after all tasks done
print('Hello Ian1')
print('Hello Ian2')
print('Hello Ian3')
loop.close()



