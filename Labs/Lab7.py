import numpy as np

a = np.array([10,20,30,40])
print(a)

b = np.arange(5)
print(b)

c = np.arange(15).reshape(3,5)
print(c)

print(c.sum(axis=0))