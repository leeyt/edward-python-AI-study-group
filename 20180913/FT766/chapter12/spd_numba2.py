import numpy as np
import time
from numba import jitclass  # import jitclass decorator
from numba import int32, float64  # import型別名稱

# 規範類別屬性的型別
spec = [
    ('size', int32),
    ('arr', float64[:]),
]


@jitclass(spec)
class RandomCode(object):

    def __init__(self, size):
        self.size = size
        self.arr = np.random.randn(size)

    def bit_code(self):
        for i in range(self.size):
            if self.arr[i] >= 0.5:
                self.arr[i] = 1
            else:
                self.arr[i] = -1
        return self.arr


if __name__ == '__main__':
    a = RandomCode(1000000)
    ts = time.clock()
    cdat = a.bit_code()
    print('程式碼生成所需時間 : {0:.3f}[s]'.format(time.clock() - ts))
