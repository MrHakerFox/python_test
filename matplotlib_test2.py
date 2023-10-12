import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.array([-3, -2, -1, 0.1, 1, 2, 3])
y = np.array([9, 4, 1, 0.1, 1, 4, 9])

ax.plot(x, y)
ax.plot(x, np.sin(x), color = (1.0, 0.2, 0.3), linestyle = '-', marker = 'o', alpha = 0.1, label = '1')
ax.plot(x, x+5, color = 'blue', linestyle = '--', marker = '^',label = '2')
ax.plot(x, x+3, color = 'g', linestyle = ':', marker = '*',label = '333')
ax.plot(x, np.cos(x), color= '0.75', linestyle= ' ', label = 'Graph')
ax.plot( 0.5 * x, y, '*--g', linewidth = 2.5,label = 'Line')

#ax.set_xlim(0, 11)
#ax.set_ylim(-5, 10)

ax.set_title( 'Заголовок нашего графика', fontsize = 20 )
ax.set_xlabel( 'Ось X' )
ax.set_ylabel( 'Ось Y' )
ax.legend( loc = 'lower left' )

ax.set_xticks(np.arange(-3, 3, 0.5))
ax.set_yticks(np.arange(-2, 10, 0.5))
ax.grid(color='gray', linewidth=2, linestyle = '-')

fig.savefig('./matplotlib_test2.png')

plt.show()