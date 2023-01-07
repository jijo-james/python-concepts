import threading
import time

# 3 different task included other than main thread_count
stime = time.time()
def task1():
    time.sleep(3)
    print("Task 1 completed")

def task2():
    time.sleep(4)
    print("Task 2 completed")

def task3():
    time.sleep(5)
    print("Task 3 completed")


'''
#calling these function in normal way
task1()
task2()
task3()

expected output
Task 1 completed
Task 2 completed
Task 3 completed
1
[<_MainThread(MainThread, started 140198328919872)>]

'''

#using multi threading - here x,y,z are threads
x = threading.Thread(target=task1, args=())
x.start()

y = threading.Thread(target=task2, args=())
y.start()

z = threading.Thread(target=task3, args=())
z.start()


# thread synchronization - main thread waits till all other threads are in sync(completed)
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
#print(time.time()-stime)

"""
op for single thread

1
[<_MainThread(MainThread, started 140267901904704)>]
"""

'''
op for multi threading

4
[<_MainThread(MainThread, started 140652723611456)>, <Thread(Thread-1 (task1), started 140652488685248)>, <Thread(Thread-2 (task2), started 140652480292544)>, <Thread(Thread-3 (task3), started 140652471899840)>]
Task 1 completed
Task 2 completed
Task 3 completed
'''

'''
op for thread synchronisation

Task 1 completed
Task 2 completed
Task 3 completed
1
[<_MainThread(MainThread, started 140598786291520)>]
274354.856180762
'''