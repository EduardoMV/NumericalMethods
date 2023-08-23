
#%%
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 1000)
plt.plot(x**2)
plt.show()
# %%
var1 = 2
var2 = 2.3
var3 = "Ejemplo"
var4 = 'Ejemplo'
var5 = [1,2,3]
var6 = ['a','b','c']
var7 = [var5,var6]
var8 = {'Dato1':10,'Data2':20,'Dato3':30}
var9 = [var7, var8]
var10 = {'Diccionario':var8,'Lista':var9}
var11 = (1,2,3,4,5)
# %%
range(10)
a = range(10)
list(range(10))
# %%
for k in range(10):
    print(k + 1)
    k += 2
# %%
for k in ['www', [1,2,3], 6]:
    print(k)
# %%
numero = 1
counts = 100000
suma = 0
for k in range(counts):
    suma = suma + numero/counts
    
print('{:.6f}'.format(suma))
print('{:.12f}'.format(suma))
print('{:.16f}'.format(suma))
print(str(suma))

# %%
print('{:<10.6f} {:<10.6f}'.format(1.2222224548948, 7.5646456))
# %%
