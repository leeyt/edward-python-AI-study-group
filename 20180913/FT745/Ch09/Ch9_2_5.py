import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df2 = df.set_index("city")
print(df2.head())
df2.head().to_html("Ch9_2_5_01.html")

df3 = df2.reset_index()
print(df3.head())
df3.head().to_html("Ch9_2_5_02.html")