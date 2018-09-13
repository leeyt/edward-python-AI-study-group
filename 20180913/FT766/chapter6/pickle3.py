import pickle
import numpy as np


def pickle_vars(fname, mode='wb', **vars):
    """
    使用方法
    pickle_vars('生成檔案的名稱', a=a, b=b, c=c)
    於引數中列舉生成檔案的名稱與物件
    """
    dic = {}
    for key in vars.keys():
        exec('dic[key]=vars.get(key)')
    with open(fname, mode) as f:
        pickle.dump(dic, f)
    return dic

if __name__ == "__main__":
    # 生成各種物件
    a = np.float(2.3)
    b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
    c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}
    # 儲存多個變數與其資料
    saved_dat = pickle_vars('pickle1.pickle', a=a, b=b, c=c)
    # 從pickle化的檔案裡取出資料
    with open('pickle1.pickle', 'rb') as f:
        dat = pickle.load(f)
        for key in dat.keys():
            exec(key+'=dat.get(key)')  # 以原本的變數還原資料
