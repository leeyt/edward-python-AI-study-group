import pandas as pd
import numpy as np

titanic = pd.read_csv("titanic_data.csv")
# 檢查PassengerId欄位是否是唯一值
print(np.unique(titanic["PassengerId"].values).size)
# 指定DataFrame物件的索引欄位
titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())
titanic.head().to_html("Ch13_5b_01.html")
# 新增SexCode欄位
titanic["SexCode"] = np.where(titanic["Sex"]=="female", 1, 0)
print(titanic.head())
titanic.head().to_html("Ch13_5b_02.html")
# PCass欄位
class_mapping = {"1st": 1,
                 "2nd": 2,
                 "3rd": 3}
titanic["PClass"] = titanic["PClass"].map(class_mapping)
print(titanic.head())
titanic.head().to_html("Ch13_5b_03.html")
# 檢查Age欄位的遺漏值有多少
print(titanic.isnull().sum())
print(sum(titanic["Age"].isnull()))
# 補值成平均值
avg_age = titanic["Age"].mean()
titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))
# 顯示性別人數和計算平均年齡
print("性別人數:")
print(titanic["Sex"].groupby(titanic["Sex"]).size())
print(titanic.groupby("Sex")["Age"].mean())
# 處理姓名欄位
import re
patt = re.compile(r"\,\s(\S+\s)") 
titles = []
for index, row in titanic.iterrows():
    m = re.search(patt, row["Name"])
    if m is None:
        title = "Mrs" if row["SexCode"] == 1 else "Mr"
    else:
        title = m.group(0)
        title = re.sub(r",", "", title).strip()
        if title[0] != "M":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
        else:
           if title[0] == "M" and title[1] == "a":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
    titles.append(title)
titanic["Title"] = titles

print("Title類別:")
print(np.unique(titles).shape[0], np.unique(titles))
# 修正類別的錯誤
titanic["Title"] = titanic["Title"].replace("Mlle","Miss")
titanic["Title"] = titanic["Title"].replace("Ms","Miss")  
titanic.to_csv("titanic_pre.csv", encoding="utf8")

print("Title人數:")
print(titanic["Title"].groupby(titanic["Title"]).size())
print("平均生存率:")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())



