import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
df.head().to_html("Ch9_3_3a_01.html")

df2 = df.sort_values("population", ascending=False)
print(df2.head())
df2.head().to_html("Ch9_3_3a_02.html")

df.sort_values(["city","population"], inplace=True)
print(df.head())
df.head().to_html("Ch9_3_3a_03.html")