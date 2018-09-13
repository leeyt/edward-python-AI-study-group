import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

# (1)產生從-π至π刻度為0.1的陣列
x = np.arange(-np.pi, np.pi, 0.1)
# 對陣列x計算sin(x)（sin()為universal函式）
y1 = sin(x)
# 對陣列x計算cos(x)
y2 = cos(x)
plt.figure(1)
plt.clf()

# 描繪x、y
plt.plot(x, y1, label='正弦函數')
plt.plot(x, y2, 'r*', markersize=10, label='餘弦函數')  # (2)
# 軸標籤設定
plt.xlabel('X軸')
plt.ylabel('Y軸')
# 圖例的繪製
plt.legend(loc='best')
# (3)繪製
plt.show()
