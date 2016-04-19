import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)
    print('Hello again!')
    return 'ok'

loop = asyncio.get_event_loop()
kaka = loop.run_until_complete(hello())
print(kaka)
loop.close()

