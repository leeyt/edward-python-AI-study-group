import pandas as pd

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "area": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                   columns=["population", "area"],
                   index=dists["name"])
print(df)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle("District Statistics")
ax.set_ylabel("Population")
ax.set_xlabel("Disticts")
ax2 = ax.twinx()
ax2.set_ylabel("Area")
df["population"].plot( ax=ax, 
                       style="b--o",
                       use_index=True,
                       rot=90)
df["area"].plot( ax=ax2, 
                 style="g-s",
                 use_index=True,
                 rot=90)