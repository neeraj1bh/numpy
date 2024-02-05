import numpy as np

from timeit import default_timer as timer

# Ax = b <=> x = A-1 b

A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])

start = timer()
x = np.linalg.inv(A).dot(b)
print(x)
end = timer()
t1 = end - start

start = timer()
end = timer()
t1 = end - start

start = timer()
x = np.linalg.solve(A, b)
print(x)
end = timer()
t2 = end - start

print(t1)
print(t2)
print(t2 / t1)
