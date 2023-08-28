#%%
import numpy as np
import matplotlib.pyplot as plt

#Shift + Enter para correrlo interactivo


# Parámetros de entrada
f = lambda x: x * np.sin(x) - 1
# Rango de nuestra función
a0 = 0.5
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


ak = 0
bk = b0
for k in range(max_iter):
    fak = f(ak)
    fbk = f(bk)
    ck = 0.5 * (ak+bk)
    fck = f(ck)
    print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, ck, ck, fak, fck, fbk))

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
#Graficación
print(Data[-1,1])
Data[:,0] #Las x
Data[:,1] #Las y

#La C (Solución) (CK) de la última fila

x = np.linspace(xmin2plot, xmax2plot, points)
y = f(x)
solLine = np.array([[ck, 2], [ck, -2]])
# solLine = np.array([[Data[-1,1],2], [Data[-1,1],-2]])
# %%
#solLine[:,0]
#solLine[:,1]
print(solLine)
print(solLine.shape)
print(Data.shape)
# %%
fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
ax.plot(x,y,label = 'Ecuación')
ax.plot(solLine[:,0], solLine[:,1], label = "Solución")
ax.plot([xmin2plot, xmax2plot], [0,0], 'r')
# ax.plot([xmin2plot, xmax2plot], [0,0], label = '_nolegend_')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')

# %%
fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
ax.plot(x,y,label = 'Ecuación')
ax.plot(solLine[:,0], solLine[:,1], label = "Solución")
ax.plot([xmin2plot, xmax2plot], [0,0], 'k')
# ax.plot([xmin2plot, xmax2plot], [0,0], label = '_nolegend_')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.set_xlim([xmin2plot, xmax2plot])