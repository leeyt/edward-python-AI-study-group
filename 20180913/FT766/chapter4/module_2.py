# 檔案名稱: module_2.py
import module_1  # import module_1並執行內部的程式


# 存取module_1內部的變數
weight = module_1.wgt
# 底下多次存取module_1內部的函式
module_1.teacher(weight)
weight = module_1.run(weight)
module_1.teacher(weight)
