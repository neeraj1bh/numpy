import numpy as np

a = np.array([[7, 8, 9, 10, 11, 12, 13], [17, 18, 19, 20, 21, 22, 23]])
print(a)

print("\n Sum \n")
print(a.sum())
print("axis=None", a.sum(axis=None))
print("axis=0 cols", a.sum(axis=0))
print("axis=1 rows", a.sum(axis=1))

print("\n Mean \n")
print(a.mean())
print("axis=None", a.mean(axis=None))
print("axis=0 cols", a.mean(axis=0))
print("axis=1 rows", a.mean(axis=1))

# variance
print("\n Variance \n")
print(a.var())
print("axis=None", a.var(axis=None))
print("axis=0 cols", a.var(axis=0))
print("axis=1 rows", a.var(axis=1))

# standard deviation
print("\n Standard Deviation \n")
print(a.std())
print("axis=None", a.std(axis=None))
print("axis=0 cols", a.std(axis=0))
print("axis=1 rows", a.std(axis=1))

print("\n Min \n")
print(a.min())
print("axis=None", a.min(axis=None))
print("axis=0 cols", a.min(axis=0))
print("axis=1 rows", a.min(axis=1))

print("\n Max \n")
print(a.max())
print("axis=None", a.max(axis=None))
print("axis=0 cols", a.max(axis=0))
print("axis=1 rows", a.max(axis=1))
