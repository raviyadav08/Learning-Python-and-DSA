import numpy as np

# a = np.array([ [6,7,8],
#                [1,2,3],
#                [9,3,2] ])
# to print all rows in a array
# for row in a:
#     print(row)

# to print a flattened version of an array
# for row in a:
#     for num in row:
#         print(num)

# another method to flatten an array using flat function
# for cell in a.flat:
#     print(cell)

# # Stacking of array can be done using np.vstack and np.hstack
# # function that takes tuples as input
# # vstack is used to stack two array vertically whereas,
# # hstack is used to stack two array horizontally.
# a = np.arange(6).reshape(3,2)
# b = np.arange(6,12).reshape(3,2)
# print("\n",a)
# print("\n",b,"\n")
# dummy = np.vstack((a,b))
# print(dummy)
# dummy = np.hstack((a,b))
# print("\n",dummy)

# Using np.hsplit can be used to split an array horizontally into different
# arrays and np.vsplit can be used to split an array vertically into different arrays

# a = np.arange(30).reshape(2,15)
# print(a)
# dummy = np.hsplit(a,5)
# print(dummy)
# dummy = np.vsplit(a,2)
# print(dummy)


# Indexing wiht boolean array
a = np.arange(12).reshape(3,4)

b = a > 4

print(b)

a[b] = -1
print(a)

