import numpy as np
import time 
import sys

"""
Numpy array takes less space as compared to list. A list takes 14 bytes 
to save a element whereas a numpy array takes 4 bytes of memory space.
This is because the numpy array stores in elements in contiguous memory
vs in python list will contain a list of pointers and then each pointer will
point to another location that stores the object and the size of it will be
14 bytes.

"""
# l = range(1000)
# print(sys.getsizeof(5)*len(l))

# array = np.arange(1000)
# print(array.size*array.itemsize)

"""
Numpy array is faster and also more convenient as compared to lists in 
python.
"""
Size = 10000000

l1 = range(Size)
l2 = range(Size)

a1 = np.arange(Size)
a2 = np.arange(Size)

#python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print(f"Python list took: {(time.time()-start)*1000}")

#numpy array
start = time.time()
result = a1 + a2
print(f"Numpy array took: {(time.time()-start)*1000}")

