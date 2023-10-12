import numpy as np
import matplotlib.pyplot as plt
fix, axes = plt.subplots(2, 2)
x = [-3, -2, -1, 0, 1, 2, 3]
y = [ 9, 4, 1, 0, 1, 4, 9 ]
x_abs = [3, 2, 1, 0, 1, 2, 3]
axes[1, 0].plot(x, y)
axes[0, 1].plot(x, x_abs)
plt.show()