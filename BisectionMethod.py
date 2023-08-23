#%%
import numpy as np

# f = lambda x: x*np.sin(x) - 1

# print(f(0))
# print(f(2))

get_c = lambda a,b: 0.5 * (a+b)

# def get_c(a,b):
#     return 0.5 * (a+b)

# print(get_c(2,3))

def f(x):
    return x*np.sin(x) - 1

print(f(0))
print(f(2))
# %%
a0 = 0
b0 = 2
fa0 = f(a0)
fb0 = f(b0)
c0 = get_c(a0,b0)
fc0 = f(c0)
#3f indica la cantidad de decimales
print('fa = {:.3f} fb = {:.3f} fc = {:.3f}'.format(fa0, fb0, fc0))
# %%
#Impresión simple
print(fa0)
#Formato de 12 decimales alineado a la izq.
print('{:<.12f}'.format(fa0))
#Formato de 12 decimales alineado a la der.
print('{:>.12f}'.format(fa0))
#Formato de 12 decimales alineado a la izq. con espacio de 20
print('{:<20.12f}'.format(fa0))
#Formato de 12 decimales alineado a la der. con espacio de 20
print('{:>20.12f}'.format(fa0))
#Con formato de string
print('{:10s} {:>3.4f}'.format('xxxxx', fa0))
# %%
print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')
print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(a0, b0, c0, fa0, fb0, fc0))
#La solución solo puede ser entre b y c por que a y c son negativos

# %%
ak = 1
bk = 2
fak = f(ak)
fbk = f(bk)
ck = get_c(ak,bk)
fck = f(ck)
print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')
print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, bk, ck, fak, fbk, fck))
#La solución solo puede ser entre a y c por que b y c son positivos, siempre el signo opuesto.
# %%
ak = 1
#Ahora cambiamos B, por que la solución estaba entre A y C
bk = 1.5
fak = f(ak)
fbk = f(bk)
ck = get_c(ak,bk)
fck = f(ck)
print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')
print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, bk, ck, fak, fbk, fck))
#La solución solo puede ser entre a y c por que b y c son positivos, siempre el signo opuesto.
# %%
ak = 1
#Ahora cambiamos B, por que la solución estaba entre A y C
bk = 1.25
fak = f(ak)
fbk = f(bk)
ck = get_c(ak,bk)
fck = f(ck)
print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')
print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, bk, ck, fak, fbk, fck))
#La solución solo puede ser entre a y c por que b y c son positivos, siempre el signo opuesto.
# %%
#Ahora, lo vamos a automatizar
# %%
