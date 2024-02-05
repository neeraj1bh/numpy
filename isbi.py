import numpy as np

# integer indexing

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

b = a[0, 1]
print(b)

b = a[0, :]  # 0th row and all cols
print(b)

b = a[:, 0]  # 0th col and all rows
print(b)

b = a[0, 1:3]  # 0th row and 1 - 3 cols 3 excluded
print(b)

b = a[0:2, 1]  # 1st col and 0 - 2 rows 2 excluded
print(b)

b = a[-1, -1]  # negative indices
print(b)

b = a[-1, 1]  # negative indices
print(b)

# boolean indexing

c = np.array([[1, 2], [3, 4], [5, 6]])
print(c)

bool_idx = c > 2
print(bool_idx)
print(c[bool_idx])
print(c[c > 2])

d = np.where(c > 2, c, -1)
print(d)

# fancy indexing

e = np.array([10, 19, 30, 41, 50, 61])
print(e)
f = [1, 3, 5]
print(e[f])
even = np.argwhere(e % 2 == 0).flatten()
print(e[even])
