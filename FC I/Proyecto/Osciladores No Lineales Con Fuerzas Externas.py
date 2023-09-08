"""
Código generado para el proyecto de Física Computacional I del Tecnológico de Costa Rica
Tema: Osciladores No Lineales Con Fuerzas Externas 
Integrantes:
    Ever Jesús Ortega Calderón
    Johnny Andrés Borbón Valverde
    Daniel Espinoza Castro
    Jesús Andrey Salazar Araya
"""

#Se importan las librerías pertinentes
#Numpy para las distintas situaciones matemáticas
#scipy.integrate para emplear la herramienta solve_ivp con la que se resolverá la EDO de segundo orden
#matplotlib.pyplot para la generación gráfica
#vpython para la generación de una visualización dinámica del sistema
import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt
from vpython import*


def F0F1(t, y):
    '''Se definen las fuciones que correspoden al lado derecho de cada ecuación
    del sistema de EDO de primer orden y[0]'=y[1]= F0(t, x)  y  y[1]'=((C*((L-h-y[0])**n)-k*(y[0]-l_0)-b*y[1])/(M)+g) = F1(t,x)
    
    Parámetros de la función
    ------------------------
    t : variable t sobre la que se desarrolla el sistema de EDO
    y : arreglo con las dos variables utilizadas para generar el sistema de EDO
    
    Salida de la función
    --------------------
    valorF0F1 : arreglo con los valores de las funciones F0(t, x) y F1(t, x)
    evaluadas en t
    '''
    
    
    
    valorF0F1 = [y[1], (C*((L-h-y[0])**n)-k*(y[0]-l_0)-b*y[1])/(M)+g]
    return valorF0F1

# Se inicializa el arreglo que contiene las dos variables del sistema de EDO
y = np.zeros(2)

# Se define el universo de valores de t de interés, que se extiende
# desde ti hasta tf y el número de valores es n
ti = 0.0
tf = 1000.0
espaciado = 200 ##Tomando como base tf= 1000 y espaciado=200, se deben reducir en proporciones iguales
t = np.linspace(ti, tf, espaciado)

# Se definen los valores iniciales de cada variable del sistema de EDO
y0 = 0.5 
y1 = 0.0

# Se establecen los valores de los parámetros propios del sistema de EDO
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

#Se genera el gráfico de la posición en función del tiempo
fig, ax = plt.subplots(dpi=120)
ax.plot(solucion_sistema_EDO.t, solucion_sistema_EDO.y[0], 'r-', label='posición ')
ax.set_title("Posición sistema oscilatorio")
ax.set_xlabel('tiempo(s)')
ax.set_ylabel('posición (m)')
plt.show()

#Se genera el gráfico de la velocidad en función del tiempo
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


#Se genera el gráfico de la aceleración en función del tiempo
fig, ax = plt.subplots(dpi=120)
ax.plot(solucion_sistema_EDO.t, aceleraciones, 'g-', label='aceleración')
ax.set_title("Aceleración sistema oscilatorio")
ax.set_xlabel('tiempo(s)')
ax.set_ylabel('aceleración (m/s^2)')
plt.show()


#Visualización dinámica

#Se genera la pantalla en la cuál se generará la visualización 
display(width=500,height=500,center=vector(0,-L/2,0),background=color.white)
#Se genera la base sobre la que se fijará el resorte
wall=box(pos=vector(0,0,0),size=vector(3/10,0.2/10,2/10),color=color.green)
#Se genera masa del problema
Mass=box(pos=vector(0,-y0,0),velocity=vector(0,0,0),size=vector(0.1,0.1,0.1),mass=M,color=color.blue)
#Punto inicial del resorte
pivot=vector(0,0,0)
#Se genera el resorte
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.01,constant=k,thickness=0.01,coils=20,color=color.red)
eq=vector(0,-0.327,0) #Posición de equilibrio


dt=(tf-ti)/espaciado
cont=0
#Se genera el movimiento del sistema para cada una de las posiciones encontradas cómo parte de la solución de la EDO
while (ti<tf):
  rate(30) #Rate perfecto 30
  vec_pos=vector(0,-solucion_sistema_EDO.y[0][cont],0)
  Mass.pos=vec_pos
  spring.axis=Mass.pos-spring.pos
  cont+=1
  ti=ti+dt
  
