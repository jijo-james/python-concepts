from multiprocessing import Process, cpu_count
import time
import csv

#import multithreading



def counter(num):
    count = 0
    while count < num :
        count += 1


a = Process(target=counter, args=(500000000,))
a.start()

b = Process(target=counter, args=(500000000,))
b.start()

a.join()
b.join()

print(time.perf_counter(), " output of m-p")




print(cpu_count())

