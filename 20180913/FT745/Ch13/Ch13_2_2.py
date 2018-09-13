import pandas as pd
from sklearn import preprocessing

f_tracking= [110, 1018, 1130, 417, 626,
             957, 90, 951, 946, 797,
             981, 125, 456, 731, 1640,
             486, 1309, 472, 1133, 1773,
             906, 532, 742, 621, 855]
happiness = [0.3, 0.8, 0.5, 0.4, 0.6,
             0.4, 0.7, 0.5, 0.4, 0.3, 
             0.3, 0.6, 0.2, 0.8, 1,
             0.6, 0.2, 0.7, 0.5, 0.7,
             0.1, 0.4, 0.3, 0.6, 0.3]

df = pd.DataFrame({"f_tracking" : f_tracking,
                   "happiness" : happiness})
print(df.head())

df_scaled = pd.DataFrame(preprocessing.scale(df), 
                         columns=["f_tracking_s", "happiness_s"])
print(df_scaled.head())
df_scaled.plot(kind="scatter", x="f_tracking_s", y="happiness_s")

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax, columns=["f_tracking_m", "happiness_m"])
print(df_minmax.head())
df_minmax.head().to_html("Ch13_2_2.html")

df_minmax.plot(kind="scatter", x="f_tracking_m", y="happiness_m")