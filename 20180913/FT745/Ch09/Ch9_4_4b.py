import pandas as pd

df1 = pd.DataFrame({"key":["a","b","b"],"data1":range(3)})  
df2 = pd.DataFrame({"key":["a","b","c"],"data2":range(3)})  
print(df1)
print(df2)
df1.to_html("Ch9_4_4b_01.html")
df2.to_html("Ch9_4_4b_02.html")

df3 = pd.merge(df1, df2)
print(df3)
df3.to_html("Ch9_4_4b_03.html")

df4 = pd.merge(df2, df1)
print(df4)
df4.to_html("Ch9_4_4b_04.html")

df5 = pd.merge(df2, df1, how='left')
print(df5)
df5.to_html("Ch9_4_4b_05.html")