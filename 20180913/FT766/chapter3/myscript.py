def my_add(x, y):
    """ 相加2個數字 """
    out = x + z  # 臭蟲：不存在變數z的定義
    return out + y

if __name__ == "__main__":
    a, b = 3, 4
    z = my_add(a, b)
    print(z)
