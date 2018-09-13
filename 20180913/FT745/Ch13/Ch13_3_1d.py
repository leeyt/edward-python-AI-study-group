import pandas as pd

df = pd.read_csv("test.csv")
# 建立布林遮罩
df1 = pd.isnull(df)
print(df1)
df1.to_html("Ch13_3_1d_01.html")