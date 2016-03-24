import time, threading, multiprocessing

def loop():
    print('Thread %s is running.' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print('Thread %s ended.' % threading.current_thread().name)



def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(i)
        finally:
            lock.release()

def deadloop():
    x = 0
    while True:
        x = x ^ 1



local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()




#Test-------------------------------------------------------------------

t1 = threading.Thread(target=process_thread, args=('Alice',))
t2 = threading.Thread(target=process_thread, args=('Ian',))

t1.start()
t2.start()
t1.join()
t2.join()



# print('Thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('Thread %s ended.' % threading.current_thread().name)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print('Balance is %d' % balance)

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=deadloop)
#     t.start()
