import pickle
import numpy as np


# 準備要儲存的物件
a = np.float(2.3)
b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}

# 將多個物件pickle至1個檔案中
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

# 從pickle化的檔案裡讀取多個物件
with open('pickle1.pickle', 'rb') as f:
    a2 = pickle.load(f)
    b2 = pickle.load(f)
    c2 = pickle.load(f)
