import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df.columns = ["直轄市", "區", "人口"]
print(df.index)
print(df.columns)
print(df.values)  