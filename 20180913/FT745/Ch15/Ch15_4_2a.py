import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

titanic = pd.read_csv("titanic.csv")
print(titanic.info())
# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic["Age"])
new_age = np.where(titanic["Age"].isnull(), 
                   age_median, titanic["Age"])
titanic["Age"] = new_age
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, 
                  titanic["SexCode"],
                  titanic["Age"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)

preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))
pd.crosstab(preds, titanic["Survived"]).to_html("Ch15_4_2a.html")

print((804+265)/(804+185+59+265))
print(logistic.score(X, y))
