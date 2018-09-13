""" Cell執行的範例 """

# %% 第1個cell : 只包含import
import numpy as np

# %% 第2個cell : 以gamma函式產生亂數
scale = 2.  # dispersion
shape = tuple(2.*np.ones(5))
adat = np.random.gamma(shape, scale=scale)
bdat = np.random.gamma(shape, scale=scale)

# %% 第3個cell : 計算乘積並print
cdat = adat * bdat
print(cdat)
