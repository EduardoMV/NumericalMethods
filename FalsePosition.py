#%%
import numpy as np
import matplotlib.pyplot as plt

#Shift + Enter para correrlo interactivo


# Parámetros de entrada
f = lambda x: x * np.sin(x) - 1
# Rango de nuestra función
a0 = 0
b0 = 2
#Para que pueda salir del ciclo x10^-6
tol = 1e-6
max_iter = 25
xmin2plot = -1
xmax2plot = 3
points = 1000

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'c', 'b', 'f(a)', 'f(c)', 'f(b)'))
print('------------------------------------------------------------')

#We create an empty matrix
Data = np.empty((0,6), float)


ak = a0
bk = b0
for k in range(max_iter):
    get_c = lambda a,b: b - f(b)*((b - a)/(f(b) - f(a)))
    fak = f(ak)
    fbk = f(bk)
    ck = get_c(ak, bk)
    fck = f(ck)
    print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, ck, bk, fak, fck, fbk))

    data = np.array([[ak, ck, bk, fak, fck, fbk]])
    Data = np.concatenate((Data, data), axis=0)


    if fak * fck < 0:
        bk = ck
    elif fbk * fck < 0:
        ak = ck
    elif (fak==0) | (fbk==0):
        print("Solución exacta encontrada")
        break
    else:
        print("Proporciona otro intervalo de inicio")
        
    if abs(fck)<=tol:
        break
# %%
