import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# (1)統計分佈函式的設定（預先Freeze）
rv = sp.stats.rayleigh(loc=1)

# (2)以上述統計分佈函式生成的亂數變數
r = rv.rvs(size=3000)

# (3)機率密度函式繪製用的百分點資料列
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 100)

# 將取樣資料的分佈與原本的機率密度函數一同繪製
plt.figure(1)
plt.clf()
plt.plot(x, rv.pdf(x), 'k-', lw=2, label='機率密度函數')
plt.hist(r, normed=True, histtype='barstacked', alpha=0.5)
plt.xlabel('值')
plt.ylabel('分佈度')
plt.show()
