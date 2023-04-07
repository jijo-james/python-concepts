#for finding the number of processors
from multiprocessing import cpu_count
print('cpu count : ', cpu_count())


#for finding python version
import sys
print('Python version : ', sys.version)

#for finding python version you can simply run the following line in terminal
# python --version
#or
# python -V

import os

home = os.path.dirname(__file__)
print(os.path.join(home, "data"))