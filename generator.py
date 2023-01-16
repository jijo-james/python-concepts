# advantages of generators
# more redability
# not holding values in memory


'''
# using fn
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_num = square_numbers([1,2,3,4,5])

#getting values on at a time
# that's how generators work
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))


# using list comprehnsion to create generators
# gerators have '()' than '[]' in list
my_num = (x*x for x in [1,2,3,4,5])

# wrapping it into a list
print(list(my_num))

# using for loop to slove repetately printing "print(next(my_num))"
for num in my_num:
    print(num)

'''



######
# calulating performance in generators

import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))
