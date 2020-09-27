import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x,y):
    return x*x + y*y

def f1(x,y):
    return 2*x

def f2(x,y):
    return 2*y

x = np.linspace( -5, 5, 200)
y = np.linspace( -5, 5, 200)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)
Z1 = f1(X,Y)
Z2 = f2(X,Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50)
ax.set_title("Q8.2.a, f(x,y)=x*x + y*y")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z1, 50)
ax.set_title("Q8.2.a, f(x,y)=x*x + y*y, df/dx")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z2, 50)
ax.set_title("Q8.2.a, f(x,y)=x*x + y*y, df/dy")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()