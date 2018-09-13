# 類別的定義
class MyClass(object):  # 無繼承類別
    """ 簡單類別範例的Docstring """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def my_print(self):
        print('{}年的奧運舉辦都市為{}'.format(self.x, self.y))

# 類別的實例化
a = MyClass(2016, '里約熱內盧')
b = MyClass(2020, '東京')
# 方法的執行
a.my_print()
b.my_print()
