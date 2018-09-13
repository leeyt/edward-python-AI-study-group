import pandas as pd

df = pd.read_csv("test.csv")
print(df)
df.to_html("Ch13_3_1.html")