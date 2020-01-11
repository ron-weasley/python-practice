import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))  # np.dot(v, w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(np.dot(x, v))  # x.dot(v)

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))  # np.dot(x, y)

print(np.sum(x))
print(np.sum(x, axis=0))  # Compute sum of each column;
print(np.sum(x, axis=1))

print(x.T)  # transpose

# Broadcasting
y = np.empty_like(x)  # Create an empty matrix with the same shape as x
vv = np.tile(v, (4, 1))
dd = np.tile(v, (4, 3))
print(y)
print(vv)
print(dd)
