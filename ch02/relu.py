import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-6, 6, 2)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1, 5)
plt.show()