import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.zeros_like(a)
print(b)

c = np.ones_like(a)
print(c)

d = np.eye(3)  
print(d)
e = np.eye(3, k=1)
print(e)
    
f = np.random.rand(3)
print(f)
g = np.random.rand(3,3)
print(g)   

