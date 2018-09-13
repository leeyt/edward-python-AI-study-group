import pandas as pd

df = pd.read_csv("test2.csv")
print(df)
df.to_html("Ch13_3_2_01.html")
