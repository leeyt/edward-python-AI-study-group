# 類別定義
class MyClass(object):  # (1)無繼承類別
    """ (2)簡單類別範例的Docstring """
    # (3)類別資料x、y的定義
    x = 0
    y = 0

    # (4)此類別的方法定義
    def my_print(self):
        # 將x視為實例裡的物件+1
        self.x += 1
        # 將y視為類別裡的物件+1
        MyClass.y += 1
        # 確認類別資料x與y的值
        print('(x, y) = ({}, {})'.format(self.x, self.y))


# 類別的實例化
f = MyClass  # (5)不加上()時僅對類別附加別名
a = MyClass()  # (6)生成MyClass類別的實例，並將其命名為a
b = f()  # (7)f()和MyClass()有著相同意義（使用別名。參考(5)）
# (8)方法的執行
a.my_print()
b.my_print()
b.my_print()
