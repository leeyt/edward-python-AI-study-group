import time


class MyTime(object):
    def __init__(self, hour, minutes, sec):
        self.hour = hour
        self.minutes = minutes
        self.sec = sec

    @staticmethod  # 將now()指定為靜態方法
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

    @staticmethod  # 將two_hours_later()指定為靜態方法
    def two_hours_later():
        t = time.localtime(time.time() + 7200)
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

# 分別以三個方法將類別MyTime進行實例化
a = MyTime(15, 20, 58)  # 使用一般的__init__進行實例化
b = MyTime.now()  # 使用靜態方法的實例化(1)
c = MyTime.two_hours_later()  # 使用靜態方法的實例化(2)
