import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.tail(3))
# 新增記錄
df.loc["third-1"] = ["台北市", "士林區", 288340]
print(df.tail(3))
df.tail(3).to_html("Ch9_4_3_01.html")
s = pd.Series({"city":"新北市","name":"中和區","population":413291})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))
df2.tail(3).to_html("Ch9_4_3_02.html")