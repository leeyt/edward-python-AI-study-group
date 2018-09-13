#程式碼9.1 Matplotlib的設定範例
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.linewidth'] = 10 # 1將線寬設定為10 points
mpl.rcParams['lines.linestyle'] = '--' # 2 將線的種類設定為虛線
mpl.rc('lines', linewidth=10, linestyle='--') # 3（與1及2相同）

t = np.arange(0, 2*np.pi, 0.1)
plt.figure(1)
plt.plot(t, np.sin(t))
plt.show()
