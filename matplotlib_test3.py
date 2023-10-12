import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
N=50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
ax.scatter(x, y, s = area, c = colors, marker = '*', cmap = 'viridis')

plt.show()