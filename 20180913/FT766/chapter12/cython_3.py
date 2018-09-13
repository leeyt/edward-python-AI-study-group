import cython_2
import numpy as np
import time

N = 10000000


# cython_2.py的函式的原始Python版本
def matrix_cal(X, Y, a):
    for i in range(N):
        if Y[i] < 0:
            Y[i] += 10.0 + 1e-7*i
    return a*X + np.exp(Y)

if __name__ == '__main__':
    # 生成用於計算的ndarray
    a = 3.4
    X = np.random.randn(N)
    Y = np.random.randn(N)
    # 以Cython版計算
    ts = time.clock()
    Z = cython_2.matrix_cal_cy(X, Y, a)
    print('Cython版的處理時間: {0:.3f}[s]'.format(time.clock() - ts))
    # 以原版的matrix_cal計算
    ts = time.clock()
    Z = matrix_cal(X, Y, a)
    print('原版的處理時間: {0:.3f}[s]'.format(time.clock() - ts))
