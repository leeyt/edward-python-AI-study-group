import pandas as pd

fruits = ["Apple","Pears","Bananas","Orange"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="Fruits")
print(s)
explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie",
       figsize=(6, 6),
       explode=explode)