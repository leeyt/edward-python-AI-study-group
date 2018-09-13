import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main1():
    """ 以多行程處理進行質數判斷 """
    ts = time.clock()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        ans = list(executor.map(is_prime, PRIMES))
    print('多行程的處理時間: {0:.3f}[s])'.format(time.clock() - ts))
    print(ans)


def main2():
    """ 以單一行程處理進行質數判斷 """
    ts = time.clock()
    ans = list(map(is_prime, PRIMES))  # 在python 3裡以list化執行計算
    print('單一行程的處理時間: {0:.3f}[s])'.format(time.clock() - ts))
    print(ans)


if __name__ == '__main__':
    main1()
    main2()
