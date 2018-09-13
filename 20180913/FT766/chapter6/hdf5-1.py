import h5py
import numpy as np

# 生成要儲存的資料
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)
dist = [2, 5, 1, 3, 8, 9, 12]

# 將部分資料以階層結構儲存
with h5py.File('data1.h5', 'w') as f:
    f.create_group('wave')
    f.create_dataset('wave/t', data=t)
    f.create_dataset('wave/y', data=y)
    f.create_dataset('dist', data=dist)

# 一旦離開with區塊 f 便會被關閉

# 資料的讀取
with h5py.File('data1.h5', 'r') as f:
    t = np.array(f['wave/t'])  # 以下均作為ndarray讀取
    y = np.array(f['wave/y'])
    dist = np.array(f['dist'])
