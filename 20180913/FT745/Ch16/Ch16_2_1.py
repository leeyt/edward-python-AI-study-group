import pandas as pd
import numpy as np
from sklearn import neighbors

X = pd.DataFrame({
   "durability": [7, 7, 3, 1],
   "strength":   [7, 4, 4, 4]
})

y = np.array([0, 0, 1, 1])
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = pd.DataFrame(np.array([[3, 7]]))
pred = knn.predict(new_tissue)
print(pred)
