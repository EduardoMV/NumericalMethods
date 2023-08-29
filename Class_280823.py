#%%
import numpy as np
#Manual Method

#Fill the table
#xSin(x) - 1 = 0
#Si dan el rango [0,2]
#

#k a c b f(a) f(b) f(c)
#0 0 2 
#1
#2
#3


f = lambda x: x*np.sin(x)-1
a0 = 0
b0 = 2
#a0 and b0 son el rango
#False position
get_c = lambda a,b: b - f(b)*((b - a)/(f(b) - f(a)))
#c es la raíz
fa0 = f(a0)
fb0 = f(b0)
c0 = get_c(a0, b0)
fc0 = f(c0)

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)'))
print('------------------------------------------------------------')
print('{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}'.format(a0, c0, b0, fa0, fc0, fb0))

#k a      c     b       f(a)       f(b)       f(c)
#0 0  1.099750  2     -1.0000    0.818595  -0.020019
#1 
#2
#3


# %%
a1 = c0
b1 = b0
fa1 = f(a1)
fb1 = f(b1)
c1 = get_c(a1,b1)
fc1 = f(c1)

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)'))
print('------------------------------------------------------------')
print('{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}'.format(a1, c1, b1, fa1, fc1, fb1))
# %%
a2 = a1
b2 = c1
fa2 = f(a2)
fb2 = f(b2)
c2 = get_c(a2,b2)
fc2 = f(c2)

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)'))
print('------------------------------------------------------------')
print('{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}'.format(a2, c2, b2, fa2, fc2, fb2))
# %%
a3 = a2
b3 = c2
fa3 = f(a3)
fb3 = f(b3)
c3 = get_c(a3,b3)
fc3 = f(c3)

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)'))
print('------------------------------------------------------------')
print('{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}'.format(a3, c3, b3, fa3, fc3, fb3))
# %%
