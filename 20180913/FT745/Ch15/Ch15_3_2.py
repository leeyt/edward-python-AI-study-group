from sklearn import datasets

boston = datasets.load_boston()

print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)
