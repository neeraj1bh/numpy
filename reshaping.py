import numpy as np

a = np.arange(1, 7)
print(a)
print(a.shape)

b = a.reshape((2, 3))
print(b)
print(b.shape)
b = a.reshape((3, 2))
print(b)
print(b.shape)

# add new axis

c = a[np.newaxis, :]
print(c)
print(c.shape)
d = a[:, np.newaxis]
print(d)
print(d.shape)
