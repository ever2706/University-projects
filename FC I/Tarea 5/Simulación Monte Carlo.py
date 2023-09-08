# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:33:43 2021

@author: Ever Ortega Calderón
"""

#Llamamos las librerías pertinentes
import numpy as np
import matplotlib.pyplot as plt
import time

tic = time.perf_counter()

###Parte A

"""
Creamos la función CaminoAleatorio3D(lista_Pos,nIter,l) que establece las posiciones aleatorias de los caminos estocásticos
Recibe:
    lista_Pos: lista que almacenará las posiciones de los caminos aleatorios
    nIter: Iteración en la que se encuentra la imulación, indica la posición 
    l: longitud media del paso
Retorna:
    lista_Pos: las posiciones del movimiento 
    longitud_paso: la norma del vector que dictará el movimiento 
"""
def CaminoAleatorio3D(lista_Pos,nIter,l):
    """
    Genera un par ordenado aleatorio respecto al punto anterior
    """
    #Se genera un valor de posición aleatorio para cada coordenada
    xPos = ((np.random.random()-0.5)*2)*l
    yPos = ((np.random.random()-0.5)*2)*l
    zPos = ((np.random.random()-0.5)*2)*l
    
    
    #Se agrega la posición nueva a la posición anterior, para así ir creando el movimiento del camino estocástico
    nuevaxPos = lista_Pos[0][nIter-1] + xPos/(np.sqrt(xPos**2+yPos**2+zPos**2))
    nuevayPos = lista_Pos[1][nIter-1] + yPos/(np.sqrt(xPos**2+yPos**2+zPos**2))
    nuevazPos = lista_Pos[2][nIter-1] + zPos/(np.sqrt(xPos**2+yPos**2+zPos**2))
    #Se agrega la posición actualizada a la lista de posiciones
    lista_Pos[0].append(nuevaxPos)
    lista_Pos[1].append(nuevayPos)
    lista_Pos[2].append(nuevazPos)

    return lista_Pos, l


###Parte c
#Se establecen parámetros iniciales
radio=1500#5*(10**8)
c=299792458
n_arbit=30
n_acumulados=0
l=5*(10**(-5))
tiempo=0
#Se crean una serie de caminos estocásticos por medio del for, para promediar lo que duran en salir del sol
for i in range(0,n_arbit):
    
    desplazamiento=0
    lista_posiciones=[[0.],[0.],[0.]]
    nPasos=1
    siga=0
    #Se ejecutará un camino hasta lograr salir del sol
    while siga==0:
        lista_posiciones,longitud_paso=CaminoAleatorio3D(lista_posiciones,nPasos,l)
        #print(nPasos)
        #Se añade la longitud del paso al desplazamiento, para cada paso 
        desplazamiento+=longitud_paso
        #Se revisa si alguna de las coordenadas logró alcanzar el radio del sol, si es así entonces se para el camino, caso contrario se sigue
        if np.abs(lista_posiciones[0][nPasos])<radio and np.abs(lista_posiciones[1][nPasos])<radio and np.abs(lista_posiciones[2][nPasos])<radio :
            nPasos+=1
            siga=0
        else:
            siga=1
    #Se suma el tiempo del camino al igual que el de la cantidad de pasos requeridos, para posteriormente promediar    
    tiempo+=desplazamiento/c
    n_acumulados+=nPasos
#Se promedia el tiempo y se calculan los años, al igual que los pasos requeridos
tiempo_promedio=tiempo/n_arbit
tiempo_años=(tiempo_promedio)*(1/60)*(1/60)*(1/24)*(1/365.25)
n_promedio=n_acumulados/n_arbit

#Se muestra al usuario los resultados de la simualción
print("Los pasos en promedio con: ",n_arbit," corridas arbitrarias, es un total de: ", n_promedio)
print("El tiempo en promedio con: ",n_arbit," corridas arbitrarias, es un total de: ", tiempo_años, " años")  
#print(lista_posiciones)
###Parte E
#Se grafica el camino estocástico del fotón
ax=plt.axes(projection="3d")
plt.figure(figsize=(10,6))
ax.plot3D(lista_posiciones[0],lista_posiciones[1],lista_posiciones[2] ,c="g", lw=0.5)
ax.set_title("Camino aleatorio del fotón")
plt.show()  

toc = time.perf_counter()


print(f"El tiempo de ejecución fue de {toc - tic:0.4f} segundos")
    
            