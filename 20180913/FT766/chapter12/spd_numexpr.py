import time
import numexpr as ne
import numpy as np

# 製作巨大的NumPy陣列
N = 10000000
a = np.random.randn(N)
b = np.random.randn(N)

# 以NumPy進行三角函數運算與累積乘加運算並量測時間
ts1 = time.clock()
c1 = (a * np.sin(b)).sum()
te1 = time.clock()
print('NumPy : %.6f [s]' % (te1 - ts1))

# 以Numexpr進行與上述相同的運算並量測時間
ts2 = time.clock()
c2 = ne.evaluate('sum(a * sin(b))')
te2 = time.clock()
print('Numexpr : %.6f [s]' % (te2 - ts2))

# 評估高速化的效果
print('%.3f[％] 較快完成處理。' % (100-100*(te2-ts2)/(te1-ts1)))
