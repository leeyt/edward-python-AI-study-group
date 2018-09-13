import numpy as np
import matplotlib.pyplot as plt
# (1)需要在scipy之外另行import
import scipy.signal as signal

# (2)Chebyshev I型的濾波器設計
b1, a1 = signal.iirfilter(4, Wn=0.2, rp=5, rs=40,
                          btype='lowpass', ftype='cheby1')
w1, h1 = signal.freqz(b1, a1)

# (3)Cauer/elliptic型的濾波器設計
b2, a2 = signal.iirfilter(4, Wn=0.2, rp=5, rs=40,
                          btype='lowpass', ftype='ellip')
w2, h2 = signal.freqz(b2, a2)

# (4)濾波器頻率特性的繪製
plt.title('頻率特性')
plt.plot(w1, 20*np.log10(np.abs(h1)), 'k-', label='Chebyshev I')
plt.plot(w2, 20*np.log10(np.abs(h2)), 'k--', label='Cauer/elliptic')
plt.legend(loc='best')
plt.ylabel('振幅 [dB]')
plt.xlabel('頻率 [rad/sample]')
plt.show()
