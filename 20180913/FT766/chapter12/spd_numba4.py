import numpy as np
from numba import jit

nthreads = 2  # 由於在2核心的CPU上驗證、將執行緒設定為2
size = 10000000


# 這是高速化之前的函式
def func_np(a, b):
    return np.exp(2.1 * a + 3.2 * b)


# 以Numba高速化之後的函式
@jit('void(double[:], double[:], double[:])', nopython=True, nogil=True)
def inner_func_nb(result, a, b):
    for i in range(len(result)):
        result[i] = np.exp(2.1 * a[i] + 3.2 * b[i])
