import matplotlib.pyplot as plt
import numpy as np
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
 
plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("Usage")
plt.title("Programming Language Usage") 
plt.show()
