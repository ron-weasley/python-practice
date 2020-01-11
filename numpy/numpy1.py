# http://cs231n.github.io/python-numpy-tutorial/
import numpy as np

# Identity
print("identity\n", np.eye(3))
print(np.eye(3,  k=1))
print(np.eye(3,2))
print(np.eye(3,2,  k=1))

print("\nzeroes\n", np.zeros((3, 3)))
print("\nones\n", np.ones((3, 3)))
print("\nfull\n", np.full((3, 3), 2))
print("\nrandom\n", np.random.random((3, 3)))
