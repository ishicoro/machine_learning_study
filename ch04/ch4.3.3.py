import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pylab as plt

def func1(x, y):
    return x**2 + y**2

x_0 = np.arange(-3, 3, 0.1)
x_1 = np.arange(-3, 3, 0.1)

X_0, X_1 = np.meshgrid(x_0, x_1)
Z = func1(X_0, X_1)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X_0, X_1, Z)
plt.show()

