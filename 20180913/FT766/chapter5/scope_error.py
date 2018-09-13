x = 10


class MyClass(object):
    x = 3  # 生成x所屬的命名空間

    def __init__(self, y):
        self.x += y

    def my_add(self, z):
        x = x + z  # 錯誤： x的scope並未被生成
        # 使用self.x便能參考


if __name__ == '__main__':
a = MyClass(10)
a.my_add(10)
print(a.x)
