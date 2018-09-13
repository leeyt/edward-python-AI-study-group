import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

print(df.tail())
print(df.tail(3)) 

df.tail().to_html("Ch9_2_3a_01.html")
df.tail(3).to_html("Ch9_2_3a_02.html") 