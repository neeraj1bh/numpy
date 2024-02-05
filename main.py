import numpy as np

print(np.__version__)

a = np.array([1, 2, 3, 4])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a[0])
a[0] = 10
print(a)

b = a * np.array([1, 2, 3, 4])
print(b)


l = [1, 2, 3]
a = np.array([1, 2, 3])

l.append(4)
l = l + [5]
print(l)
l *= 2
print(l)


# a.append(4)
print(a)
a = a + np.array([4])
print(a)
a *= 2
print(a)
a += 2
print(a)
