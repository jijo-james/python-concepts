from contextlib import contextmanager
import os


'''
#example 1
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('sample_text.txt', 'w') as f:
    f.write('Writing something...')


print(f.closed)
'''

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('class'):
    print(os.listdir())

with change_dir('sample'):
    print(os.listdir())

# for switching and saving current directories context manager is useful 
# rather than typing it each time