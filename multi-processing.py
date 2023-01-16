from multiprocessing import Process, cpu_count
import time
import csv

#import multithreading

start = time.perf_counter()

def counter(num):
    count = 0
    while count < num :
        count += 1


a = Process(target=counter, args=(300000000,))
a.start()
print(300000000)

b = Process(target=counter, args=(300000000,))
b.start()

c = Process(target=counter, args=(300000000,))
c.start()

#d = Process(target=counter, args=(250000000,))
#d.start()

a.join()
b.join()
c.join()
#d.join()

finish = time.perf_counter()

print(finish - start)


print(cpu_count())

