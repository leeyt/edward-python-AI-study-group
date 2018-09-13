import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)
df.to_html("Ch13_3_3a_01.html")