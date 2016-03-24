
from multiprocessing import Process, Pool, Queue

import os, time, random, subprocess

def run_proc(name):
    print('Run process %s in %s of parent %s' % (name, os.getpid(), os.getppid()))

def long_time_task(name):
    print('Run task %s in %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f second.' % (name, (end-start)))


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # print('Parent process %s.' % os.getpid())
    # # p = Process(target=run_proc, args=('test',))
    # p = Pool(4)
    #
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    #
    # print('Wait for all subprocesses done')
    # p.close()
    # p.join()
    # print('All subprocesses done.')

    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')

    # print('$ nslooup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code is %s' % r)

    # print('$ nslookup')
    # p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE,
    #                      stderr=subprocess.PIPE)
    #
    # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode(encoding='utf-8'))
    # print('Exit code:', p.returncode)

    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


