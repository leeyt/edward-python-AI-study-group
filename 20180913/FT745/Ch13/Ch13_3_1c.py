import pandas as pd

df = pd.read_csv("test.csv")
# 填補遺失資料
df1 = df.fillna(value=1)
print(df1)
df1.to_html("Ch13_3_1c_01.html")

df["B"] = df["B"].fillna(df["B"].mean())
print(df)
df.to_html("Ch13_3_1c_02.html")

df["C"] = df["C"].fillna(df["C"].median())
print(df)
df.to_html("Ch13_3_1c_03.html")
