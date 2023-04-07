'''
# code1
def decorator_func(original_func):
    def wrapper_func():
        print('wrapper_func executed this before {} function'.format(original_func.__name__))
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print('Display function run succesfully')

display()

#this is the conventional method for running but the one above is the best
"""
def display():
    print('Display function run succesfully')

decorator_display = decorator_func(display)
decorator_display()
"""
'''








'''
## two functions using one decorator one with and one without arguments
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper_func executed this before {} function'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def display():
    print('Display function run succesfully')

@decorator_func
def display_info(name, age):
    print('display_info ran with variables ({}, {})'.format(name,age))

display()
display_info('Jijo', 25)
'''







'''
## decorator class
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper_func executed this before {} function'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func

class DecoratorClass(object):

    def __init__(self, original_func):
        self.original_func = original_func
    
    def __call__(self, *args, **kwargs):
        print('call method(DecoratorClass) executed this before {} function'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@DecoratorClass
def display():
    print('Display function run succesfully')

@decorator_func
def display_info(name, age):
    print('display_info ran with variables ({}, {})'.format(name,age))

display()
display_info('Jijo', 25)
'''






# using multiple decorators with wrap function
from functools import wraps


def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)

    return wrapper


def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('ALLEN', age=23)
# The above line is equivalent to dispaly_info = my_logger(my_timer(display_info))