import numpy as np

""" How to print elements of an array """
arr1 = np.arange(6)   # Create a 1d array of elements from 0 to 5
arr2 = np.arange(12).reshape(4,3)  # create a 2d array of 12 elements from 0 to 11 and reshape it as a 3 by 4 array
arr3 = np.arange(24).reshape(2, 3, 4)   # create a 3d array of 24 elements from 0 to 23 and reshape it as a 2 by 3 by 4 array
""" Print the dirst element of each array """
print("The first element of arr1 is: ", arr1[0])
print("The first element of arr2 is: ", arr2[0])
print("The first element of arr3 is: ", arr3[0])

""" Prin the first index of each array """
print("The first element of arr1 at index 1 is: ", arr1[0])           # For 1d 
print("The first element of arr2 at index 1 is: ", arr2[0][0])        # For 2d
print("The first element of arr3 at index 1 is: ", arr3[0][0][0])     # For 3d

""" Simple operation on the index level """

print(arr1[2]+arr2[0]) # add the third element of arr1 to the first element of arr2
print(arr2[1]+arr2[2]) # both elements have the same size 
# print(arr2[2] + arr3[1]) #both array don't have the same size
# But if it is an array of one element, we can add it to any other array
print(arr2[1][1] + arr3[1][2])
#Same we can multiply a number by any size of an array
print(2*arr1)
# The dot prodcut of an matrix

""" Multiplication of matrix """
A = np.arange(4).reshape(2,2)
B = np.arange(2 , 6).reshape(2,2)
print("The First matrix is: ", A)
print("The second matrix is :", B)

print("The product of the element are :", A*B)
print("The maxtrix product is :", A@B)
print("The dot product of A and B is :", A.dot(B))
print("The maximun element in A is : ", A.max())
print("The minimum element of row are: ", A.min(1))
print("The maximum element of colunm are: ", A.max(0))
print("The sum of elements in A is : ", A.sum())
print("The average element in A is: ", A.mean())

print("The sum of each colunm in  B is: ", B.sum(axis =0))
print("The sum of each row in  B is: ", B.sum(axis =1))
print("The cumulative sum of the elements along each row", B.cumsum(axis=1))