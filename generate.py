import numpy as np

a = np.zeros((5))
print(a)
print(a.dtype)

a = np.zeros((5, 2))
print(a)
print(a.dtype)

a = np.ones((2, 5))
print(a)
print(a.dtype)

a = np.full((5, 5), 5)
print(a)
print(a.dtype)


# identity matrix

a = np.eye((5))
print(a)
print(a.dtype)

a = np.linspace(0, 10, 5)
print(a)
print(a.dtype)

a = np.linspace((0, 1), 5)
print(a)
print(a.dtype)
