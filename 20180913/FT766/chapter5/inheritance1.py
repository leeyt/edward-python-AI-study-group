# (1)類別MyBase的定義（MyDeriv的基礎類別）
class MyBase(object):
    coeff = 2

    def __init__(self, x):
        self.x = x

    def mult(self):
        return self.coeff * self.x


# (2)類別MyDeriv的定義（MyBase的衍生類別）
class MyDeriv(MyBase):
    coeff = 3  # (3)重新定義屬性

    # (4)重新定義建構函式
    def __init__(self, x, y):
        super().__init__(x)  # (5)基礎類別方法的呼叫範例
        self.y = y  # (6)新增屬性y並在實例化時初始化

    # (7)增加新的方法（mult方法則為繼承得來）
    def mult2(self):
        return self.coeff * self.x * self.y


# (8)使用MyBase與MyDeriv的計算範例
a = MyBase(3)  # 生成MyBase的實例
print(a.mult())  # 結果為 2*3=6
b = MyDeriv(3, 5)  # 生成MyDeriv的實例
print(b.mult())  # 結果為 3*3=9 （確認繼承得來的方法）
print(b.mult2())  # 結果為 3*5*5=45（確認新增的方法）
