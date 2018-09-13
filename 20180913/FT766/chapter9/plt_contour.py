import numpy as np
import matplotlib.pyplot as plt
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

# --- 製作繪圖
plt.figure(1)

# (1)將z値以顏色的深淺表示
im = plt.imshow(z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3, 3, -2, 2))

# (2)顯示等高線
levels = np.arange(-3, 2.5, 0.5)
ctr = plt.contour(z, levels, colors='k', origin='lower',
                  linewidths=2, extent=(-3, 3, -2, 2))

# (3)於等高線表示其標籤
plt.clabel(ctr, levels, inline=1, colors='black',
           fmt='%1.1f', fontsize=14)
plt.show()
