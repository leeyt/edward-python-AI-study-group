import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df.columns = ["直轄市", "區", "人口"]
print(df.head(4)) 
df.head(4).to_html("Ch9_2_3b.html")