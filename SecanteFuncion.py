import numpy as np

def secante_method(f, x0, x1, tol=1e-6, max_iter=5):
    print('{:<9s} {:<9s} {:<9s} {:<9s} {:<9s}'.format('x0', 'x1', 'nextX', 'f(x0)', 'f(x1)'))
    print('------------------------------------------------------------')

    for k in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        nextX = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        fnextX = f(nextX)

        print('{:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f} {:<9.6f}'.format(x0, x1, nextX, fx0, fx1))

        if abs(fnextX) <= tol:
            break

        x0 = x1
        x1 = nextX

    return nextX

# Función
f = lambda x: x * np.sin(x) - 1

# Puntos de inicio
x0 = 11
x1 = -3

# Queremos 5 iteraciones, por lo tanto
max_iter = 5

# Llamar a la función para encontrar la raíz
root = secante_method(f, x0, x1, tol=1e-6, max_iter=max_iter)

print('La raíz aproximada es:', root)
