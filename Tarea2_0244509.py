#%%
import numpy as np
import matplotlib.pyplot as plt
# %%
#Problema 1
#Método de bisección

#Función
f = lambda x: ((3/25)*(x**3)) + ((139/100)*(x**2)) - ((161/60)*(x)) - (539/18)

#Intervalo de inicio
a0 = -15
b0 = 6  

#Queremos 5 iteraciones, por lo tanto
tol = 1e-6
max_iter = 5

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')

ak = a0
bk = b0

#Empezamos el ciclado del método de bisección
for k in range(max_iter):
    fak = f(ak)
    fbk = f(bk)
    ck = 0.5 * (ak+bk)
    fck = f(ck)
    print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, bk, ck, fak, fbk, fck))

    if fak * fck < 0:
        bk = ck
    elif fbk * fck < 0:
        ak = ck
    elif (fak==0) | (fbk==0):
        print("Solución exacta encontrada")
        break

    if abs(fck)<=tol:
        break

# %%
#Problema 2
#Método de posición falsa

#Función
f = lambda x: ((3/25)*(x**3)) + ((139/100)*(x**2)) - ((161/60)*(x)) - (539/18)

#Intervalo de inicio
a0 = -15
b0 = 6  

#Queremos 5 iteraciones, por lo tanto
tol = 1e-6
max_iter = 5

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'))
print('------------------------------------------------------------')

ak = a0
bk = b0

#Empezamos el ciclado del método de posición falsa
for k in range(max_iter):
    get_c = lambda a,b: b - f(b)*((b - a)/(f(b) - f(a)))
    fak = f(ak)
    fbk = f(bk)
    ck = get_c(ak, bk)
    fck = f(ck)
    print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(ak, bk, ck, fak, fbk, fck))


    if fak * fck < 0:
        bk = ck
    elif fbk * fck < 0:
        ak = ck
    elif (fak==0) | (fbk==0):
        print("Solución exacta encontrada")
        break
        
    if abs(fck)<=tol:
        break
# %%
#Problema 3
#Método de Secante

#Función
f = lambda x: ((3/25)*(x**3)) + ((139/100)*(x**2)) - ((161/60)*(x)) - (539/18)

#Queremos 5 iteraciones más la iniciadora, por lo tanto
tol = 1e-6
max_iter = 6

print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('xk', 'x1', 'nextX', 'f(xk)', 'f(x1)'))
print('------------------------------------------------------------')

#Puntos de inicio
x0 = -10
x1 = 1

#Empezamos el ciclado del método de secante
for k in range(max_iter):
        fxk = f(x0)
        fx1 = f(x1)

        nextX = x1 - fx1 * ((x1 - x0) / (fx1 - fxk))
        fnextX = f(nextX)

        print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(x0, x1, nextX, fxk, fx1))

        if abs(fnextX) <= tol:
            break

        x0 = x1
        x1 = nextX


# %%
#Problema 4
#Método de Newton-Raphson

#Función
f = lambda x: ((3/25)*(x**3)) + ((139/100)*(x**2)) - ((161/60)*(x)) - (539/18)

#Para el método de Newton-Raphson tenemos que derivar, por lo tanto
df = lambda x: ((9/25)*(x**2)) + ((139/50)*(x)) - (161/60)

#Queremos 5 iteraciones, por lo tanto
tol = 1e-6
max_iter = 5

print('{:<9s} {:<9s} {:<9s}'.format('xk', 'f(xk)', 'f\'(xk)'))
print('-----------------------------')

#Solo necesitamos un punto, por lo tanto
xk = -10

for k in range(max_iter):
        fxk = f(xk)
        dfxk = df(xk)

        if abs(dfxk) < tol:
            print("Derivada cercana a cero. El método no converge.")

        print('{:<9.6f} {:<9.6f} {:<9.6f}'.format(xk, fxk, dfxk))

        if abs(fxk) <= tol:
            break

        xk = xk - fxk / dfxk

# %%
#Problema 5 (Tasa de Interés)
#Aplicación: Metodo de Secante

#Datos del problema
P = 2500000 #Prestamo inicial  
A = 20000 #Pago mensual fijo
n = 15 * 12 #15 años, lo que sería 180 meses

#Número de iteraciones aproximado (10)
tol = 1e-6
max_iter = 10

#Tomando en cuenta que es un caso de aplicación de la vida real, podemos estimar que el interés se encuentra entre el 1% y el 15%
i0 = 0.01 #1% de interés
i1 = 0.15 #15% de interés

# Listas para almacenar los valores de las tasas de interés y los resultados en cada iteración
intereses = []
resultados = []

#El interés máximo que el usuario pagará
i_max = 0.0

for _ in range(max_iter):
    result_i0 = (A / ((1 + i0)**(1/12) - 1)) * (1 - (1 + i0)**-(n/12)) - P
    result_i1 = (A / ((1 + i1)**(1/12) - 1)) * (1 - (1 + i1)**-(n/12)) - P


    intereses.append(i1)  # Almacena la tasa de interés actual
    resultados.append(result_i1)  # Almacena el resultado actua

    # Cálculo de la siguiente aproximación de la tasa de interés utilizando el método de la secante
    i_next = i1 - result_i1 * (i1 - i0) / (result_i1 - result_i0)

    #Comprobación de convergencia
    if abs(i_next - i1) < tol:
        i_max = i_next
        break

    i0 = i1
    i1 = i_next

tasaInteres = i_max * 100
print(f"La máxima tasa de interés que puede pagar es del {tasaInteres:.2f}%")
# %%
#Creamos e inicializamos los valores de la gráfica, 0.01 siendo el interés inicial y 0.15 el máximo interés, y 100 puntos que se generan entre los intereses.
x = np.linspace(0.01, 0.15, 100)

# Cálculo de los valores de la función de iteración (y) para cada valor de tasa de interés en el rango.
# Esta es la ecuación de interés que calculé arriba.
y = (A / ((1 + x) ** (1 / 12) - 1)) * (1 - (1 + x) ** (-n / 12)) - P

solLine = np.array([[i_max, 2], [i_max, -2]])

fig, ax = plt.subplots(figsize=(10, 6))

# Gráfico de la función de iteración
ax.plot(x, y, label='Ecuación')
ax.plot(solLine[:, 0], solLine[:, 1], label="Solución", marker='o', linestyle='--')
ax.plot([0.01, 0.15], [0, 0], 'r', linestyle='--')

ax.legend()
ax.set_xlabel('Tasa de Interés')
ax.set_ylabel('Resultado de la función de iteración')
ax.set_title('Interés máximo que el usuario pagará')
ax.grid(True)

plt.show()

tasaInteres = i_max * 100
print(f"La máxima tasa de interés que puede pagar es del {tasaInteres:.2f}%")
# %%
