import numpy as np
from memory_profiler import profile


@profile  # 底下的函式是記憶體profiler的分析對象
def func_a():
    a = np.random.randn(500, 500)
    return a**2


@profile  # 底下的函式是記憶體profiler的分析對象
def func_b():
    a = np.random.randn(1000, 1000)
    return a**2


def func_both():
    a = func_a()
    b = func_b()
    return [a, b]

if __name__ == '__main__':
    func_both()
