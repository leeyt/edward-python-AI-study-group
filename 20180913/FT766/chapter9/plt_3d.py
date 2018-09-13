from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.mlab import bivariate_normal

# 製作2維格子
N = 200
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)
X, Y = np.meshgrid(x, y)

# 以2變量常態分佈製作2維分佈資料
z = 15 * (bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0) -
          bivariate_normal(X, Y, 1.5, 0.5, 1, 1))

# 將資料立體繪製
fig = plt.figure(1)  # (1)
ax = fig.add_subplot(111, projection='3d')  # (2)
surf = ax.plot_surface(X, Y, z, cmap=cm.gray)
ax.set_zlim3d(-3.01, 3.01)
plt.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
