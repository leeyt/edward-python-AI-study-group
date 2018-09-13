import numpy as np
import scipy as sp

# 生成要儲存的資料
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)

# MAT-file的寫入範例
out_dat = {}
out_dat['time'] = t  # 將ndarray的t以名稱time儲存
out_dat['y'] = y
sp.io.savemat('data2.mat', out_dat, format='5')

# MAT-file的讀取範例
matdat = sp.io.loadmat('data1.mat', squeeze_me=True)
tt = matdat['time']  # 生成ndarray
