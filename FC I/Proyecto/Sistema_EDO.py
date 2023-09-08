# coding=utf-8
# Ejemplo tomado del Klein (sección 8.8)

import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt


def F0F1(t, y):
    '''Se definen las fuciones que correspoden al lado derecho de cada ecuación
    del sistema de EDO de primer orden y[0]'=F0(t, y) y y[1]'=F1(t, y)
    
    Parámetros de la función
    ------------------------
    t : variable t sobre la que se desarrolla el sistema de EDO
    y : arreglo con las dos variables utilizadas para generar el sistema de EDO
    
    Salida de la función
    --------------------
    valorF0F1 : arreglo con los valores de las funciones F0(t, y) y F1(t, y)
    evaluadas en t
    '''
    
    
    
    valorF0F1 = [y[1], (C*((L-h-y[0])**n)-k*(y[0]-l_0)-b*y[1])/(M)+g]
    return valorF0F1

# Se inicializa el arreglo que contiene las dos variables del sistema de EDO
y = np.zeros(2)

# Se define el universo de valores de t de interés, que se extiende
# desde ti hasta tf y el número de valores es n
ti = 0.0
tf = 7.0
espaciado = 100
t = np.linspace(ti, tf, espaciado)

# Se definen los valores iniciales de cada variable del sistema de EDO
y0 = 0.35
y1 = 0.0

# Se establecen los valores de los parámetros beta y omega del sistema de EDO
C= 2.3*(10**(-4))  
L= 0.8
h= 0.035
n= -2.53
k= 10.42
l_0= 7.1*(10**(-2))
b=2.96*(10**(-3))
M= 0.2579
g= 9.8

# Se calcula la solución del sistema de EDO utilizando la biblioteca SciPy
metodoRK = 'RK45'
solucion_sistema_EDO = spint.solve_ivp(F0F1, [ti, tf], [y0, y1], t_eval=t, method=metodoRK)

#print(solucion_sistema_EDO)

fig, ax = plt.subplots(dpi=120)
ax.plot(solucion_sistema_EDO.t, solucion_sistema_EDO.y[0], 'r-', label='posición ')
ax.set_title("Posición sistema oscilatorio")
ax.set_xlabel('tiempo(s)')
ax.set_ylabel('posición (m)')
plt.show()

fig, ax = plt.subplots(dpi=120)
ax.plot(solucion_sistema_EDO.t, solucion_sistema_EDO.y[1], 'b-', label='velocidad')
ax.set_title("Velocidad sistema oscilatorio")
ax.set_xlabel('tiempo(s)')
ax.set_ylabel('velocidad (m/s)')
plt.show()


"""
Obtención de la aceleración apartir de la ecuación de movimiento
"""
aceleraciones=[]
for i in range(0,len(solucion_sistema_EDO.y[0])):
    nueva_aceleracion=((C*((L-h-solucion_sistema_EDO.y[0][i])**n) -k*(solucion_sistema_EDO.y[0][i]-l_0) -b*solucion_sistema_EDO.y[1][i])/(M) +g)
    aceleraciones.append(nueva_aceleracion)



fig, ax = plt.subplots(dpi=120)
ax.plot(solucion_sistema_EDO.t, aceleraciones, 'g-', label='aceleración')
ax.set_title("Aceleración sistema oscilatorio")
ax.set_xlabel('tiempo(s)')
ax.set_ylabel('aceleración (m/s^2)')
plt.show()

print(solucion_sistema_EDO.y[0])
print(solucion_sistema_EDO.y[1])
print(aceleraciones)