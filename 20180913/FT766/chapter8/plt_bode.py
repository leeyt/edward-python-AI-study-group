import scipy as sp
import matplotlib.pyplot as plt

# (1)需要在scipy之外另行import
from scipy import signal

# (2)線性系統的定義
s1 = sp.signal.lti([1], [1, 1])

# (3)使用bode函式解析
w, mag, phase = sp.signal.bode(s1)

# (4)波德圖的描繪
plt.figure(1)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Bode magnitude plot
plt.box('on')
plt.xlabel('頻率 [rad/s]')
plt.ylabel('增益 [dB]')
plt.title('波德圖')
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Bode phase plot
plt.xlabel('頻率 [rad/s]')
plt.ylabel('位相 [deg]')
plt.box('on')
plt.show()
