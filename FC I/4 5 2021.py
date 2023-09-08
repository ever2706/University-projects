# -*- coding: utf-8 -*-
"""
Created on Tue May  4 09:40:50 2021

@author: Ever Ortega Calderón
"""

"""
#Ejercicio 1
import numpy as np

N=10000000

nTiros=N

nAciertos=0

for i in range(0,nTiros):
    x=np.random.random()
    y=np.random.random()
    circulo=x**2+y**2
#Menor o igual a uno, debido a que se producen numeros random entre 0 y 1 entonces el radio sería 1, 
#pensando en un cuarto del circulo pues está centrado en (0,0), radio 1 y el  x**2+y**2 me dará positivo, es decir primer cuadrante
    if circulo<=1:
        nAciertos+=1

print("Aciertos: ", nAciertos)

#Cuando los tiros tienden a infinito yo habré llenado todo el cuadrado con puntos entonces puedo decir que nTiros es el area del cuadrado 
area_cuadrado=nTiros

area_circulo=nAciertos

pi=4*(area_circulo/area_cuadrado)

print("Pi es: ",pi)



#Ejercicio 2
import numpy as np
import matplotlib.pyplot as plt
N=8192
aleatorios_ala2=0
iteraciones=[]
uno_raizn=[]
for i in range(1,N+1):
    #Genero números aleatorios, uno por integral
    aleatorios=0
    for j in range(0,10):
        aleatorios+=np.random.random()
        
    aleatorios_ala2+=aleatorios**2
    iteraciones.append(i)
    uno_raizn.append(1/np.sqrt(i))
#resultado=(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1-0)*(1/N)*aleatorios_ala2
resultado=(1/N)*aleatorios_ala2

print(resultado)

fig,ax=plt.subplots(1,1,dpi=150)
ax.plot(iteraciones,uno_raizn, c="m", lw=0.5)
ax.set_title("Aproximación integral por Monte Carlo")
plt.show()


#Ejercicio 3 (Ejercicio 2, con otra integral) 
import numpy as np
import matplotlib.pyplot as plt

def Funcion(x):
    fun=np.exp(np.sqrt(x**3 + 5*x))
    return fun

def Sumatoria(iteraciones_N):
    suma=0
    for i in range(1,iteraciones_N+1):
        numero_alea=np.random.random()
        suma+=Funcion(numero_alea)
    return suma
        
        
def Aproximacion_Monte_Carlo(a,b,iteraciones_N):
    aprox=(b-a)*(1/iteraciones_N)*Sumatoria(iteraciones_N)
    return aprox
        
def Grafica(iteraciones_N):
    uno_entre_raizn=[]
    iteraciones=np.linspace(1,iteraciones_N,iteraciones_N)
    for i in range(1,iteraciones_N+1):
        uno_entre_raizn.append(1/np.sqrt(i))
    fig,ax=plt.subplots(1,1,dpi=150)
    ax.plot(iteraciones,uno_entre_raizn, c="m", lw=0.5)
    ax.set_title("Aproximación integral por Monte Carlo")
    plt.show()

N=8192
aproximacion=Aproximacion_Monte_Carlo(0,1,N)
Grafica(N)
print("La aproximación de la integral por Monte Carlo con un N de: ",N," es: ",aproximacion)
"""

#Ejercicio 4 (Ejercicio 2 y 3 con otra integral)
"""
Buenas profe. Soy Ever del curso de Física Computacional. Es que estaba intentando hacer la integral que usted puso hoy en clase, la que iba de 0 a infinito.
Pero tenía una duda, porque los números random que yo evalúe en la función tienen que estar entre 0 e inf, o sea que pueden ser números muy grandes, 
evaluados en la función da números muy pequeños, tan pequeños que el programa los da como cero y restringiendo un poco para que no tire números random 
tan grandes, resulta que no da la integral porque la estoy multiplicando por (b-a) que es muy muy grande, or ende para que me de bien necesito que la 
sumatoria dé muy pequeña, entonces ni una ni otra, esto significa que el método no funciona tan bien para integrales inf o qué estoy entendiendo mal?
"""

    
import numpy as np
import matplotlib.pyplot as plt
import math 
from random import uniform

pseudo_infi=1000000000000000
def Funcion(x):
    fun=np.exp(-x**2)
    return fun

def Sumatoria(iteraciones_N,b):
    suma=0
    for i in range(1,iteraciones_N+1):
        #numero_alea=np.random.random()
        numero_alea=float(uniform(0,b))
        suma+=float(Funcion(numero_alea))
    return suma
        
        
def Aproximacion_Monte_Carlo(a,b,iteraciones_N):
    aprox=(b-a)*(1/iteraciones_N)*Sumatoria(iteraciones_N,b)
    return aprox
        
def Grafica(iteraciones_N):
    uno_entre_raizn=[]
    iteraciones=np.linspace(1,iteraciones_N,iteraciones_N)
    for i in range(1,iteraciones_N+1):
        uno_entre_raizn.append(1/np.sqrt(i))
    fig,ax=plt.subplots(1,1,dpi=150)
    ax.plot(iteraciones,uno_entre_raizn, c="m", lw=0.5)
    ax.set_title("Aproximación integral por Monte Carlo")
    plt.show()

N=819120
#Si yo uso ahí inf entonces la aproximación me va a dar infinita ¿aló?
#¿Es porque los números random deben estar entre 0 e inf?
aproximacion=Aproximacion_Monte_Carlo(0,pseudo_infi,N)
Grafica(N)
print("La aproximación de la integral por Monte Carlo con un N de: ",N," es: ",aproximacion)    
    
    