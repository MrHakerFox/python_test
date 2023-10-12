import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

ax.hist(x, 50, density=True, facecolor = 'g', alpha=0.75)
plt.show()