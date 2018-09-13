import numpy as np  # 匯入NumPy
import csv  # 匯入標準模組csv


# 讀取自CSV檔案
dat = np.loadtxt('data1.csv', delimiter=',', skiprows=1, dtype=float)

# 將ndarray的dat寫入至CSV檔案（請留意無法處理中文）
np.savetxt('data1_saved.csv', dat, fmt='%.1f,%.8f,%d',
           header='time,vel,alt', comments='')

# 將ndarray的dat寫入至CSV檔案（也能處理中文）
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('time,速度,高度\n')
    writer = csv.writer(f)
    writer.writerows(dat)
