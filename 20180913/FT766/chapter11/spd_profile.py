import cProfile
import numpy as np
import pstats


def is_prime(a):
    """ 質數判斷程式（費馬小定理） """
    a = abs(a)
    if a == 2:
        return True
    if a < 2 or a & 1 == 0:
        return False
    return pow(2, a-1, a) == 1


def mysum(n):
    """ 計算從1到N的整數的和 """
    return np.arange(1, n+1).sum()


def task1(n):
    """ 執行底下的2個處理
       (1) 從1到N的整數當中尋找質數
       (2) 計算從1到N的整數的和
    """
    # (1)
    out = []
    append = out.append
    for k in range(1, n+1):
        if is_prime(k):
            append(k)
    # (2)
    a = mysum(n)
    return [out, a]


def task2(n):
    """ 計算從1到N的sqrt() """
    return np.sqrt(np.arange(1, n+1))


def main():
    task1(100000)  # 負荷較大的處理
    task2(100000)  # 負荷較小的處理


if __name__ == '__main__':  # (3)
    cProfile.run('main()', filename='main.prof')
    sts = pstats.Stats('main.prof')
    sts.strip_dirs().sort_stats('cumulative').print_stats()
