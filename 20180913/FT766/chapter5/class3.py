# (1)於全域命名空間裡定義x
x = 100


class MyClass:
    # (2)作為此類別的資料定義i與x
    i = 10  # 在方法price()裡被參考
    x += 2  # 將全域命名空間裡的x加上2來定義資料x
    xx = x + 2  # (3)參考MyClass裡的資料x
    print('xx = ', xx)

    def price(self):
        y = self.i * x  # (4)參考全域命名空間裡的物件x
        z = self.i * self.x  # (5)依實例屬性→類別屬性的順序來搜尋並參考
        # z = i * x  # (6)這裡會發生錯誤（在此無法看到資料i）
        print("price y = %d" % y)
        print("price z = %d" % z)

    def shop(self):
        # price()  # (7)會發生錯誤（NameError）
        self.price()  # (8)這個方式OK
        # MyClass.price(self) # (9)這個方式也OK
        MyClass.i = 20  # (10)變更類別的資料
        print("方法 shop 結束")


# (11)用來確認動作的程式碼
if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.shop()  # 當中會執行 MyClass.i = 20
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
    a.i = 2  # 設定實例屬性
    MyClass.i = 4  # 變更類別屬性
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
