import pandas as pd

titanic = pd.read_csv("titanic_data.csv")
# 顯示前5筆
print(titanic.head())
titanic.head().to_html("Ch13_5a_01.html")
# 顯示統計摘要資訊
print(titanic.describe())
titanic.describe().to_html("Ch13_5a_02.html")
# 顯示資料集資訊
print(titanic.info())
