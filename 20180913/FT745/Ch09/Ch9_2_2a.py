import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("dists.csv", encoding="utf8")
print(df)
df.to_html("Ch9_2_2a_01.html")
# 匯入JSON格式的檔案
df2 = pd.read_json("dists.json")
print(df2)
df.to_html("Ch9_2_2a_02.html")