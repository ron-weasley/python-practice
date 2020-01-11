import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
a = np.array([1, 0, 2])

print("slice\n",arr[0:2, 1:3]) # OR arr(arr[:2, 1:3])

print("\narange\n", arr[np.arange(3), a])

print("\nadd(+)\n",arr+a)
arr[np.arange(3), a] +=a
print("\narr\n",arr)