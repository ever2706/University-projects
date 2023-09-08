# coding=utf-8
# Ejemplo tomado del Landau 2012 (sección 17.3)

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def U0(x,lado):
    '''Se define el potencial eléctrico que existe en el borde de la placa

    Parámetros de la función
    ------------------------
    x : posición a lo largo del borde

    Salida de la función
    --------------------
    valorU0 : valor del potencial eléctrico en la posición x
    '''

    valorU0 = 25 + (75*x)/lado

    return valorU0

def Em(m,lado):
    em,error=integrate.quad(lambda x: (1/np.sinh(m*np.pi))*U0(x,lado)*np.sin((m*np.pi*x)/lado),0,lado)
    #print(em)
    return em

def AproxUXY(x, y, lado, nt):
    '''Calcula el valor aproximado del potencial eléctrico en el punto (x, y)

    Parámetros de la función
    ------------------------
    x : posición en el eje x (o posiciones si se suministra un arreglo)
    y : posición en el eje y (o posiciones si se suministra un arreglo)
    lado : arista de la placa cuadrada sujeta al potencial eléctrico
    nt : número de términos que tendrá el cálculo del potencial (debe ser
           mayor o igual que 1)

    Salida de la función
    --------------------
    valorAproxUXY : valor del potencial eléctrico en el punto (x, y)
    '''

    # Se inicializa el valor del potencial eléctrico a calcular
    valorAproxUXY = 0

    # Se realiza la sumatoria que corresponde con el número de términos dado
    for i in range(1, nt+1):
        # Se genera el contador impar que requiere la sumatoria
        nimpar = i
        m=i
        valorAproxUXY += (Em(m,lado))*np.sin(nimpar*np.pi*x/lado)*np.sinh(nimpar*np.pi*y/lado)
        
    return valorAproxUXY

# Se define el valor de la arista de la placa cuadrada sujeta al potencial
# eléctrico
longitudarista = 1

# Se indica el número de términos para el cálculo de la aproximación del
# potencial eléctrico
numeroterminos = 5

# Se define la malla de puntos para evaluar el potencial eléctrico
puntosmalla = 30
x = np.linspace(0, longitudarista, puntosmalla)
y = np.linspace(0, longitudarista, puntosmalla)
X, Y = np.meshgrid(x, y)

# Se calcula el valor aproximado del potencial eléctrico en los puntos de
# la malla y se asignan al eje Z
Z = AproxUXY(X, Y, longitudarista, numeroterminos)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('U (V)')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='cividis', edgecolor='none')
ax.set_title('Aproximacion potencial electrico en la placa');
fig.savefig("04 Ecuaciones Diferenciales Parciales - AP potencial 2D.png")
