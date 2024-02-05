import numpy as np

a = np.array([1, 2, 3])
b = a
print(a)

b[0] = 42
print(b)
print(a)

c = a.copy()
c[0] = 1
print(c)
print(a)
