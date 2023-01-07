from multiprocessing import Process, cpu_count
import time
import csv

#import multithreading



def counter(num):
    count = 0
    while count < num :
        count += 1


a = Process(target=counter, args=(1000000000,))
a.start()

a.join()

print(time.perf_counter(), " output of m-p")




print(cpu_count())

