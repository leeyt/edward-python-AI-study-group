from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
print(iris.data.shape)
print(iris.feature_names)
print(iris.DESCR)
