import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
# 取得與更新單筆記錄
print(df.loc[ordinals[1]])
s = ["新北市", "新莊區", 416640] 
df.loc[ordinals[1]] = s
print(df.head(3))
df.head(3).to_html("Ch9_4_1a.html")