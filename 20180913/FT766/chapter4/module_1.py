# 檔案名稱: module_1.py """
print("module_1 is imported.")
wgt = 60.5  # 初始體重 [kg]


def teacher(x):
    if x > 60:
        print("過重")
    else:
        print("正常體重")

def run(weight):
    print("跑步減重了1kg")
    weight -= 1
    return weight

