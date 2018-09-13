import numpy as np
import matplotlib.pyplot as plt

# (1)由於名稱略長附加別名
import scipy.interpolate as ipl


# (2)原本的函數定義
def f(x):
    return (x-7) * (x-2) * (x+0.2) * (x-4)

# (3)生成原始資料（正解的值）
x = np.linspace(0, 8, 81)
y = np.array(list(map(f, x)))

# (4)補值前的寬刻度資料
x0 = np.arange(9)
y0 = np.array(list(map(f, x0)))

# (5)設定補值函式（線性補值）
#  設定補值函式（線性補值／3次樣條）
f_linear = ipl.interp1d(x0, y0, bounds_error=False)
f_cubic = ipl.interp1d(x0, y0, kind='cubic', bounds_error=False)
#  補值處理的執行
y1 = f_linear(x)  # 線性補值
y2 = f_cubic(x)  # 3次樣條補值

# (6)補值資料與原始資料的比較繪製
plt.figure(1)
plt.clf()
plt.plot(x, y, 'k-', label='原始函數')
plt.plot(x0, y0, 'ko', label='補值前資料', markersize=10)
plt.plot(x, y1, 'k:', label='線性補值', linewidth=4)
plt.plot(x, y2, 'k--', label='3次樣條補值', linewidth=4, alpha=0.7)
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.show()