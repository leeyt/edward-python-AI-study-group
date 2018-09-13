import matplotlib.pyplot as plt
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
 
plt.pie(ratings, labels=labels)
plt.title("Programming Language Usage") 
plt.axis("equal")
plt.show()
