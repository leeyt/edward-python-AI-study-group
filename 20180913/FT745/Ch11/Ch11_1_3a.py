import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=1, high=7, size=num_throws)
    mask = (throws == 1)
    probability_of_throws = len(throws[mask])/num_throws    
    results.append(probability_of_throws)
	
df = pd.DataFrame({"throws" : results})

df.plot(color="r")
plt.title("Law of Large Numbers")
plt.xlabel("Number of throws in sample")
plt.ylabel("Average Of Sample")

