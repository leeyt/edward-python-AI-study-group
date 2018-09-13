import pandas as pd
from sklearn import datasets

boston = datasets.load_boston()

X = pd.DataFrame(boston.data, columns=boston.feature_names)
print(X.head())
X.head().to_html("Ch15_3_2.html")
target = pd.DataFrame(boston.target, columns=["MEDV"])
print(target.head())
target.head().to_html("Ch15_3_2a.html")