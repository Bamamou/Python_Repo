import numpy as np  # this is how the numpy package can be imported
a =np.arange(15).reshape(3,5)  # this means take numbers from 0 to 14 and arrange them in an array of 3 by 5
print(a)
""" The Shape of the array a """
a.shape     # This method returns the shape of an array
print("The shape of the a array is:", a.shape)

""" The dimension of array """
a.ndim       # this method returns the dimension of the array
print("The dimension od the array is:", a.ndim)

""" The data type of of the array """
a.dtype.name  # it returns the data type of the array
print("The data type of the aray is: ", a.dtype.name)

""" The size of the items in the array """
a.itemsize      # it returns the size of the items in the array
print("The size of the item size is:", a.itemsize)

""" The size of the array itself """
a.size          # it returns the size of the array (numbe of elements in the array)
print("The size of the array is:", a.size)   

""" The type of the array """
type(a)          #It returns the data type of the argument
print("a is a: ", type(a))


""" How to create a one dimensional array in numpy """
arr1 = np.array([2, 5, 8])  #This is how a numpy array can be created 
print(arr1)
arr2 =np.array([2.3, 5.5, 8, 10.4])
print("The data type of arr2 is: ", arr2.dtype)
print("The dimension of arr2 is: ", arr2.ndim)

""" How to create a two dimensional array in numpy """
arr3 =np.array([[(1, 2, 3), (5, 4 , 9)], [(2, 3, 6), (0, 8, 1)]])  # this is a two dimensional array 
print("The dimension or arr3 is :", arr2.ndim)

""" How to create an arry of zeros , ones or empty """
arr4 =np.zeros((3,4))
print(arr4)
print("the size of arr4 is:", arr4.size)
print("the data type of arry4 is :", arr4.dtype)
print("the dimension of arr4 is: ", arr4.ndim)
print("the items' size in arr4 is :", arr4.itemsize)

arr5 =np.ones((4,4))
print(arr5)
print("the size of arr5 is:", arr5.size)
print("the data type of arry5 is :", arr5.dtype)
print("the dimension of arr5 is: ", arr5.ndim)
print("the items' size in arr5 is :", arr5.itemsize)
print("the shape of arr5 is :", arr5.shape)

arr6 =np.empty((5,5))
print(arr6)
print("the size of arr6 is:", arr6.size)
print("the data type of arry6 is :", arr6.dtype)
print("the dimension of arr6 is: ", arr6.ndim)
print("the items' size in arr6 is :", arr6.itemsize)
print("the shape of arr6 is :", arr6.shape)

"""  How to create an array with a specifiv datatype """
arr7 = np.array( [  [1, 3], [5, 8]], dtype=complex)
arr8 = np.array([[(1, 2),(5, 8),(2,9)],[(5,2),(0,7),(9,4)]], dtype = float)
print("the data type of arr7 is : ", arr7.dtype)
print("The data type of arr8 is : ", arr8.dtype)

""" How to use the create an array using the arang function """
# The arange function is similar to the python built-in range function but returns an array instead of list
arr9 = np.arange(10, 50, 5) # it creates an array starting from 10 to 50-5 with a step of 5 
arr10 = np.arange(0, 2, 0.2) # creates an aray from 0 to 10-0.2 with 0.2 as step 
print("arr9 is: ", arr9)
print("arr10 is: ", arr10)
""" We can also create array using the linespace function """
# for that we first need to import the pi subpackage of numpy
from numpy import pi
arr11 = np.linspace(0, 2 ,9)        #mean create an array with 9 numbers from 0 to 2
arr12 = np.linspace(0, 2*pi, 100)   # create an array of 100 numbers from 0 to 2pi (360)
print("arr11 is: ", arr11)
print("arr12 is: ", arr12)
