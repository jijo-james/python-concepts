# Python program to measure elapsed time in python


# # method 1
# import time

# start = time.time()

# print(23*2.3)

# end = time.time()
# print(end - start)


# method 2
from timeit import default_timer as timer

start = timer()

print(23 * 2.3)

end = timer()
print("elapsed time: ", end - start)
