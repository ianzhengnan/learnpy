
import time, queue

from multiprocessing.managers import BaseManager
from multiprocessing import Queue

class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '192.168.73.130' #Connect Mac OS
print('Connect to server %s...' % server_addr)

m = QueueManager(address=(server_addr,5000), authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.empty:
        print('Task queue is empty.')

print('Worker exit.')


