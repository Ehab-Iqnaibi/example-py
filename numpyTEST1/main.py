import numpy as np
#import math
def fun (x):
    return x**2
def integrate(f,a,b,n):
    dx=(b-a)/n
    x=np.linspace(a+dx/2,b-dx/2,n)
    fx=f(x)
    area=np.sum(fx)*dx
    return area

print(integrate(np.sin, 0, np.pi/2, 100))
print(integrate(np.sin, 0, np.pi*2, 100))
print(integrate(fun, 0, 3, 100))
'''

#print(np.__version__)
list1=[c for c in range(10)]
anp=np.array(list1)
print(anp)

lst_2d = [[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11]]
a_2d = np.array(lst_2d)
print(a_2d)
lst_3d = [[[0, 1], [2, 3]],
         [[4, 5], [6, 7]],
          [[8, 9], [10,11]] ]
a_3d = np.array(lst_3d)
print(a_3d)
print(a_3d.shape)
print(a_3d[1, 0, 1])
print(a_3d[2, 1, 0])
'''