# matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 10**9)
# plt.plot(n, 7 * n * n * n + 6 * n + 5)
plt.plot(n,(((8 * n + 1) ** 0.5 - 1) / 2), label="((8n+1)^0.5 - 1)/2")
plt.plot(n,(2*n ** 0.5), label="2*n^0.5")
plt.legend(loc='upper left')
plt.show()
