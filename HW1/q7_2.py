import numpy as np
import matplotlib.pyplot as plt

h = (2*np.pi) / 1000
x = np.linspace(-np.pi, np.pi, 1000)

y1 = np.sin(x) + x*np.cos(x)
y2 = (((x+h)*np.sin(x+h)) - (x*np.sin(x)))/h


plt.plot(x, y1, label = "y1 = np.sin(x) + x*np.cos(x)")
plt.plot(x, y2, label = "y2 = (((x+h)*np.sin(x+h)) - (x*np.sin(x)))/h")
plt.title("Q7, Derivates of x*sin(x)")
plt.legend()
plt.show()