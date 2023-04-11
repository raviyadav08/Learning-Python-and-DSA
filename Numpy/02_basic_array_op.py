import numpy as np

# Creating a 2 dimensional array
# dtype= is used to change the elements 
a = np.array([[1,2],[3,4],[5,6]])

# Used to print number of dimensions of an array
print(f'No.of dimensions in array: {a.ndim}')

# Used to print the size of the elements that is present in an array
print("Item size of elements in array: ",a.itemsize)

# dtype= is used to change the datatype of elements present in the array
a = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print("Item size of elements in array after changing datatype: ",a.itemsize)

# size is used to represent the total number of elements in the array
print("Size of the array:",a.size)

# shape represents the information on dimension of array 
# similar to no of rows and coloumns present in array 
print("Shape of array: ",a.shape)

# you can use dtype to represent complex numbers
a = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print("\n",a,"\n")

# zeroes function is used for inputting array with zeroes in it and 
# by providing the shape of the array after it.
print("Array filled with 0")
dummy = np.zeros((3,4))
print(f"\n{dummy}\n")

# similarly you can use ones function to input array with ones in it
print("Array filled with 1")
dummy = np.ones((3,4))
print(f"\n{dummy}\n")

# arrange is similar to range but is used with arrays
dummy = np.arange(1,5,2)
print(f"\n{dummy}\n")

# linspace is used for generating numbers from between start and 
# end numbers and no of nums you want to generate in an array.
dummy = np.linspace(1,10,5)
print(f"\n{dummy}\n")

# You can reshape your arrays using reshape function
dummy = a.reshape(2,3)
print(f"\n{dummy}\n")

# You can use ravel function to flatten your array into 1d array
dummy = a.ravel()
print(f"\n{dummy}\n")

a = np.array([[1,2],
              [3,4],
              [5,6]])

"""
Mathematical functions that you can do in array 
1. min()
2. max()
3. sum()
4. np.sqrt(arr_name)
5. np.std(arr_name) ---standard deviation
In sum you can use axis in order to perform sum on rows or coloums
axis = 0 is used for coloumn level sum whereas,
axis = 1 is used for row level sum.
"""
print(a.min())
print(a.max())
print(a.sum(axis= 0))
print(a.sum(axis = 1))
print(np.sqrt(a))
print('\n')


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print("\n",b,"\n")

# Operations that you can perform in an array....
print(a+b)
print(a-b)
print(a*b)
print(a/b)


