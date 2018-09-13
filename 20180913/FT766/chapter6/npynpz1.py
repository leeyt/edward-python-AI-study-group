import numpy as np

# 將1個ndarray儲存於npy
a = np.array([1, 2, 3])
np.save('foo', a)

# 從npy還原ndarray
a2 = np.load('foo.npy')

# 將ndarray輸出至npz（多個ndarray的壓縮檔）
b = np.array([[1, 2], [3, 4]])
np.savez('foo.npz', a=a, b2=b)  # 將b以名稱b2儲存

# npz檔案的輸入
with np.load('foo.npz') as data:
    a3 = data['a']  # 只取出名為a的變數
    b3 = data['b2']
