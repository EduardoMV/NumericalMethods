#%%
import numpy as np

f = lambda x: x * np.sin(x) -1 

get_nextX = lambda x0, x1: x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))

x0 = 11
x1 = -3
fx0 = f(x0)
fx1 = f(x1)
nextX = get_nextX(x0,x1)
#Nuestra solución
fnextX = f(nextX)

print('x0 = ' + str(x0))
print('x1 = ' + str(x1))
print('nextX = ' + '%.6f'%nextX)
print('f(x0) = ' + str(fx0))
print('f(x1) = ' + str(fx1))
#Nuestra solución
print('f(nextX) = ' + str(fnextX))

# %%
x0 = x1
x1 = nextX
fx0 = f(x0)
fx1 = f(x1)
nextX = get_nextX(x0,x1)
#Nuestra solución
fnextX = f(nextX)

print('x0 = ' + str(x0))
print('x1 = ' + str(x1))
print('nextX = ' + '%.6f'%nextX)
print('f(x0) = ' + str(fx0))
print('f(x1) = ' + str(fx1))
#Nuestra solución
print('f(nextX) = ' + str(fnextX))
# %%
x0 = x1
x1 = nextX
fx0 = f(x0)
fx1 = f(x1)
nextX = get_nextX(x0,x1)
#Nuestra solución
fnextX = f(nextX)

print('x0 = ' + str(x0))
print('x1 = ' + str(x1))
print('nextX = ' + '%.6f'%nextX)
print('f(x0) = ' + str(fx0))
print('f(x1) = ' + str(fx1))
#Nuestra solución
print('f(nextX) = ' + str(fnextX))
# %%
x0 = x1
x1 = nextX
fx0 = f(x0)
fx1 = f(x1)
nextX = get_nextX(x0,x1)
#Nuestra solución
fnextX = f(nextX)

print('x0 = ' + str(x0))
print('x1 = ' + str(x1))
print('nextX = ' + '%.6f'%nextX)
print('f(x0) = ' + str(fx0))
print('f(x1) = ' + str(fx1))
#Nuestra solución
print('f(nextX) = ' + str(fnextX))
# %%
x0 = x1
x1 = nextX
fx0 = f(x0)
fx1 = f(x1)
nextX = get_nextX(x0,x1)
#Nuestra solución
fnextX = f(nextX)

print('x0 = ' + str(x0))
print('x1 = ' + str(x1))
print('nextX = ' + '%.6f'%nextX)
print('f(x0) = ' + str(fx0))
print('f(x1) = ' + str(fx1))
#Nuestra solución
print('f(nextX) = ' + str(fnextX))
# %%