class MyCalc(object):
    @staticmethod
    def my_add(x, y):
        return x + y

a = MyCalc.my_add(5, 9)  # 結果將是 a = 14（不需要生成MyCalc的實例）
