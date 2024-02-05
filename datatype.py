import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print(a)
print(a.dtype)

b = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

print(b)
print(b.dtype)

c = np.array([1.0, 2.0, 3.0, 4, 5, 6])

print(c)
print(c.dtype)

d = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=np.int64)

print(d)
print(d.dtype)
