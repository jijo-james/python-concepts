import logging
logging.basicConfig( level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running {} with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,4)
sub_logger(10,2)

# example 2
"""
def outer_func(msg):
    def inner_func():
        print (msg)
    return inner_func

hi_fn = outer_func('Hiiii...')
bye_fn = outer_func('Bye.....')

hi_fn()
bye_fn()
"""