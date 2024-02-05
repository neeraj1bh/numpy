import numpy as np

b = np.array([1, 2, 3])
print(b.shape)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# access

print(a[0])
print(a[0][0])
print(a[0, 0])

# slice

print(a[0, :])
print(a[:, 0])

# transpose

print(a.T)
print(a.T.T)


# inverse

c = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(c))

# determinant
print(np.linalg.det(c))


# diagonal matrix
d = np.diag(c)
print(d)
# returns a 1D vector

print(np.diag(d))
