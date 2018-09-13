from numba import jit
import numpy as np
import time


def mult_abs_basic(n, x, y):
    r = []
    for i in range(n):
        r.append(abs(x[i] * y[i]))
    return r


def mult_abs_numpy(x, y):
    return np.abs(x*y)


# 以@jit decorator試著高速化
@jit('f8[:](i8, c16[:], c16[:])', nopython=True)
def mult_abs_numba(n, x, y):
    r = np.zeros(n)
    for i in range(n):
        r[i] = abs(x[i] * y[i])
    return r


if __name__ == "__main__":
    # %% 生成處理資料
    N = 1000000
    x_np = (np.random.rand(N) - 0.5) + 1J * (np.random.rand(N) - 0.5)
    y_np = (np.random.rand(N) - 0.5) + 1J * (np.random.rand(N) - 0.5)
    x = list(x_np)
    y = list(y_np)

    # %% 處理時間比較
    ts = time.clock()
    b1 = mult_abs_basic(N, x, y)
    print('Python的計算時間 : {0:0.3f}[s]'.format(time.clock() - ts))
    ts = time.clock()
    b1 = mult_abs_numpy(x_np, y_np)
    print('NumPy的計算時間 : {0:0.3f}[s]'.format(time.clock() - ts))
    ts = time.clock()
    b1 = mult_abs_numba(N, x_np, y_np)
    print('Numba的計算時間 : {0:0.3f}[s]'.format(time.clock() - ts))
