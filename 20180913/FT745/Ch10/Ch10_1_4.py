import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend()
plt.xlabel("Rads")
plt.ylabel("Amplitude")
plt.title("Sin and Cos Waves")
plt.show()

