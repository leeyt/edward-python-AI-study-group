import pandas as pd

fruits = ["Apple","Pears","Bananas","Orange"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="Fruits")
print(s)
s.plot(kind="pie")