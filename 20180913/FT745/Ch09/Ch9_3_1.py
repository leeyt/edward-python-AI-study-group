import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df["population"].head(3))
print(df[["city","name"]].head(3))
df[["city","name"]].head(3).to_html("Ch9_3_1.html")

print(df.population.head(3))   # 使用屬性方式
