import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))
print(df.loc[:,["name","population"]].head(3))
df.loc[:,["name","population"]].head(3).to_html("Ch9_3_1b_01.html")

print(df.loc["third":"fifth", ["name","population"]])
print(df.loc["third", ["name","population"]])
df.loc["third":"fifth", ["name","population"]].to_html("Ch9_3_1b_02.html")
# 取得單一純量值
print(df.loc[ordinals[0], "name"])
print(type(df.loc[ordinals[0],"name"]))
print(df.loc["first", "population"])
print(type(df.loc["first", "population"]))
