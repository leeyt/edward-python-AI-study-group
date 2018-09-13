import pandas as pd

df = pd.read_csv("test2.csv")
print(df.duplicated())

print(df.duplicated("B"))
