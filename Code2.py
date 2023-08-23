#%%
import numpy as np
import matplotlib.pyplot as plt

# fig1 = plt.figure(1)
# fig1.clf()
#Borrar
fig2 = plt.figure(2)
fig2.clf()

# ax1 = fig1.add_subplot(1,1,1)

ax2 = fig2.add_subplot(1,2,1)
ax3 = fig2.add_subplot(2,2,2)
ax4 = fig2.add_subplot(2,2,4)
# ax5 = fig2.add_subplot(2,2,4)

x = np.linspace(-5, 5, 40)
y1 = x**2
y2 = 0.5*x

ax2.plot(x, y1)
ax2.plot(x, y2)

ax3.plot(x,y1,lw=2,ls='-',color=(1, 0, 1))
ax3.plot(x, y2,lw=2,ls='-.', color=(0,1,0))
ax3.grid(True)
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.legend(['Parabola', 'Recta'])

ax4.plot(x,y1,lw=2,ls='-',color=(0, 0, 0))
ax4.plot(x, y2,lw=2,ls='-.', marker='.', ms = 10, mec=(0,0,1), mfc=(1,0,0), color=(0,1,0))
ax4.grid(False)
ax4.set_xlabel('x')
ax4.set_ylabel('y')

# plt.show(fig1, fig2)
plt.show(fig2)

# %%
