#  %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# n = np.linspace(1, 100)
# plt.plot(n, 7 * n * n * n + 6 * n + 5)
# plt.show()

# n = np.linspace(1, 100)
# plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
# plt.plot(n, 20 * n, label="20n")
# plt.legend(loc='upper left')
# plt.show()

n = np.linspace(3.32*10**122, 3.34*10**122)
plt.plot(n, n ** .1, label="n^.1")
plt.plot(n, np.log(n) ** 5, label="(log n)^5")
plt.legend(loc='upper left')
plt.show()
