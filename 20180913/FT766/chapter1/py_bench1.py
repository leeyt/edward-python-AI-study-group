import numpy as np
import time


def mult_basic(N, M, L, a, x, y):
    """ 不使用矩陣運算而以for迴圈來計算的函式
        但由於要建立所需大小的非ndarray有困難，
        輸入的變數使用NumPy的ndarray傳入 """
    r = np.empty((N, L))
    for i in range(N):
        for j in range(L):
            tmp = 0.0
            for k in range(M):
                tmp = tmp + a[k]*x[i][k]*y[k][j]
            r[i][j] = tmp
    return r


def mult_fast(N, M, L, a, x, y):
    """ 使用NumPy的函式來進行高速計算的函式
        和函式mult_basic得到完全相同的結果 """
    return np.dot(x*a, y)  # 處理的記述僅需1行


if __name__ == '__main__':
    # 產生計算用的陣列
    np.random.seed(0)
    N = 10000
    M = 1000
    L = 10000
    a = np.random.random(M) - 0.5
    x = np.random.random((N, M)) - 0.5
    y = np.random.random((M, L)) - 0.5

    # 不使用矩陣運算而以for迴圈來計算
    ts = time.time()
    r1 = mult_basic(N, M, L, a, x, y)
    te = time.time()
    print("Basic method : %.3f [ms]" % (1000*(te - ts)))

    # 使用NumPy的函式來進行高速計算
    ts = time.time()
    r2 = mult_fast(N, M, L, a, x, y)
    te = time.time()
    print("Fast method  : %.3f [ms]" % (1000*(te - ts)))
