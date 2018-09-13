import pandas as pd

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates("B")
print(df1)
df1.to_html("Ch13_3_2c_01.html") 

df2 = df.drop_duplicates("B", keep="last")
print(df2)
df2.to_html("Ch13_3_2c_02.html") 

df3 = df.drop_duplicates("B", keep=False)
print(df3)
df3.to_html("Ch13_3_2c_03.html") 