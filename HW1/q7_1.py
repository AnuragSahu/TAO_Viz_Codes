import numpy as np
import matplotlib.pyplot as plt

h = (0.2 - 0.1) / 500
x = np.linspace(0.1, 0.2,500)

y1 = -1/(x*x)
y2 = ((1/(x+h))- (1/x))/h

plt.plot(x, y1, label = "y1 = -1/(x*x)")
plt.plot(x, y2, label = "y2 = ((1/(x+h))- (1/x))/h")
plt.title("Q7, Derivates of 1/x")
plt.legend()
plt.show()