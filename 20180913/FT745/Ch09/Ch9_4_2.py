import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
# 刪除純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = None
print(df.iloc[1,2])
df.iloc[1,2] = None
print(df.head(3))
df.head(3).to_html("Ch9_4_2.html")