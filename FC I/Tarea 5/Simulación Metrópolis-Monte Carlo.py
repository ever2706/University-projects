# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:29:44 2021

@author: Ever Ortega Calderón
"""

import numpy as np
import matplotlib.pyplot as plt

"""
#Creación de espines de forma de abajo
def Creacion_espines(numEspines):
    espines=[]
    for i in range(numEspines):
        espines.append(-1)
    return espines


#Creación de espines de forma de arriba
def Creacion_espines(numEspines):
    espines=[]
    for i in range(numEspines):
        espines.append(1)
    return espines

"""
#Creación de espines de forma random
def Creacion_espines(numEspines):
    espines=np.random.randint(-1,1,size=numEspines)
    for i in range(numEspines):
        if espines[i]==0:
            if np.random.random()>0.5:
                espines[i]=1
            else:
                espines[i]=-1
    return espines

def Energia(arreglo_Espines,valorJ):
    energia=0
    for i in range (len(arreglo_Espines)-1):
        energia+=arreglo_Espines[i]*arreglo_Espines[i+1]
        #print (energia)
    return -valorJ*energia

def Magnetizacion(arreglo_Espines):
    magnetico=0
    for i in arreglo_Espines:
        magnetico+=i
    return magnetico

def CambioDeEspin(arreglo_Espines,numero_Espines):
    posicion_Alea=np.random.randint(numero_Espines)
    if arreglo_Espines[posicion_Alea]==1:
        arreglo_Espines[posicion_Alea]=-1
    else:
        arreglo_Espines[posicion_Alea]=1
    #return posicion_Alea,arreglo_Espines
    return arreglo_Espines

     
    
######

nPasos=10
numero_Espines=3

valorJ=1
kBoltzman=1
temperatura=1
espinesi=Creacion_espines(numero_Espines)
#print(espinesi)
espines_Grafico=[]
espines_Grafico.append(np.array(espinesi))

for m in range(nPasos):
    energiai=Energia(espinesi,valorJ)
    #num_espin,espinesj=CambioDeEspin(espinesi,numero_Espines)
    espinesj=CambioDeEspin(espinesi,numero_Espines)
    energiaj=Energia(espinesj,valorJ)
    deltaE=energiaj-energiai
    pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
    if deltaE>0:
        if np.random.random()<pAceptacion:
            #pass
            espines_Grafico.append(np.array(espinesj))
        else:
            espines_Grafico.append(np.array(espinesi))
            #espinesi[num_espin]*=-1
    else:
        #pass
        espines_Grafico.append(np.array(espinesj))
    #espines_Grafico.append(np.array(espinesi))

arreglo_Grafico=np.asarray(espines_Grafico)
"""
Pregunta: con "esperar a que la simulación entren en equilibrio" se refiere a hacerlo en este momento? es decir una vez que los espines se cambiaron? 
"""
momento_magnetico=Magnetizacion(arreglo_Grafico)
energia=Energia(arreglo_Grafico,valorJ)
#print(momento_magnetico)
print(arreglo_Grafico)
print(energia)
#print(arreglo_Grafico)

ejecuciones=10
energias_acumuladas=0
magneticos_acumulados=0
for i in range (0,ejecuciones):
    arreglo_Grafico=np.asarray(espines_Grafico)
    magneticos_acumulados+=Magnetizacion(arreglo_Grafico)
    energias_acumuladas+=Energia(arreglo_Grafico,valorJ)
    #print(Energia(arreglo_Grafico,valorJ))

"""
Pregunta: obtengo una energía para cada espín, eso está bien?
"""
#print(energias_acumuladas)
#print(magneticos_acumulados)
energia_prom= energias_acumuladas/ejecuciones
magnetico_prom=magneticos_acumulados/ejecuciones
#print(energia_prom)
#print(magnetico_prom)
"""
Pregunta: parte e) qué carajos dice esa fórmula de U. ¿Es el promedio de la energía de los tres espines?
"""

#Parte f
kBoltzman=0.001
magneticos_varios_kBT=[]
kBTs=[]
while kBoltzman<=5:
    nPasos=10
    numero_Espines=3
    
    valorJ=1
    
    temperatura=1
    espinesi=Creacion_espines(numero_Espines)
    #print(espinesi)
    espines_Grafico=[]
    espines_Grafico.append(np.array(espinesi))
    
    for m in range(nPasos):
        energiai=Energia(espinesi,valorJ)
        #num_espin,espinesj=CambioDeEspin(espinesi,numero_Espines)
        espinesj=CambioDeEspin(espinesi,numero_Espines)
        energiaj=Energia(espinesj,valorJ)
        deltaE=energiaj-energiai
        pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
        if deltaE>0:
            if np.random.random()<pAceptacion:
                #pass
                espines_Grafico.append(np.array(espinesj))
            else:
                espines_Grafico.append(np.array(espinesi))
                #espinesi[num_espin]*=-1
        else:
            #pass
            espines_Grafico.append(np.array(espinesj))
        #espines_Grafico.append(np.array(espinesi))
    
    arreglo_Grafico=np.asarray(espines_Grafico)
    """
    Pregunta: con "esperar a que la simulación entren en equilibrio" se refiere a hacerlo en este momento? es decir una vez que los espines se cambiaron? 
    """
    momento_magnetico=Magnetizacion(arreglo_Grafico)
    energia=Energia(arreglo_Grafico,valorJ)
    #print(arreglo_Grafico)
    
    ejecuciones=10
    energias_acumuladas=0
    magneticos_acumulados=0
    for i in range (0,ejecuciones):
        arreglo_Grafico=np.asarray(espines_Grafico)
        magneticos_acumulados+=Magnetizacion(arreglo_Grafico)
        #energias_acumuladas+=Energia(arreglo_Grafico,valorJ)
    
    """
    Pregunta: obtengo una energía para cada espín, eso está bien?
    """
    #print(energias_acumuladas)
    #print(magneticos_acumulados)
    #energia_prom= energias_acumuladas/ejecuciones
    magnetico_prom=magneticos_acumulados/ejecuciones
    magneticos_varios_kBT.append(magnetico_prom)
    kBTs.append(kBoltzman)
    kBoltzman+=1

"""
Pregunta sobre práctica f: wtf, tengo un arreglo de valores en ktb y una matriz para los valores de magnetico, cómo gráfico eso? aló?
"""    
#print(np.asarray(magneticos_varios_kBT))
#print(np.asarray(kBTs))

"""
Parte g: qué?????? 
"""


"""
fig,ax=plt.subplots(figsize=[10,10],dpi=120)
ax.imshow(arreglo_Grafico.T,"plasma")
ax.set_title("Simulación del modelo de Ising 1-D")
ax.set_label("Pasos")
ax.set_ylabel("espines")
ax.set_aspect("5")
plt.show()

#################################
def ModeloIsing(temperatura):
    def Creacion_espines(numEspines):
        espines=np.random.randint(-1,1,size=numEspines)
        for i in range(numEspines):
            if espines[i]==0:
                if np.random.random()>0.5:
                    espines[i]=1
                else:
                    espines[i]=-1
        return espines
    
    def Energia(arreglo_Espines,valorJ):
        energia=0
        for i in range (len(arreglo_Espines)-1):
            energia+=arreglo_Espines[i]*arreglo_Espines[i+1]
        return -valorJ*energia
    
    def CambioDeEspin(arreglo_Espines,numero_Espines):
        posicion_Alea=np.random.randint(numero_Espines)
        if arreglo_Espines[posicion_Alea]==1:
            arreglo_Espines[posicion_Alea]=-1
        else:
            arreglo_Espines[posicion_Alea]=1
        #return posicion_Alea,arreglo_Espines
        return arreglo_Espines
    
         
        
    ######
    
    nPasos=10
    numero_Espines=3
    
    valorJ=1
    kBoltzman=1
    #temperatura=1
    espinesi=Creacion_espines(numero_Espines)
    espines_Grafico=[]
    espines_Grafico.append(np.array(espinesi))
    lista_Energias=[]
    lista_Energias.append(Energia(espines_Grafico,valorJ))
    for m in range(nPasos):
        energiai=Energia(espinesi,valorJ)
        #num_espin,espinesj=CambioDeEspin(espinesi,numero_Espines)
        espinesj=CambioDeEspin(espinesi,numero_Espines)
        energiaj=Energia(espinesj,valorJ)
        deltaE=energiaj-energiai
        pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
        if deltaE>0:
            if np.random.random()<pAceptacion:
                #pass
                espines_Grafico.append(np.array(espinesj))
                energiaActual=Energia(espinesj,valorJ)
                lista_Energias.append(energiaActual)
            else:
                espines_Grafico.append(np.array(espinesi))
                energiaActual=Energia(espinesi,valorJ)
                lista_Energias.append(energiaActual)
                #espinesi[num_espin]*=-1
        else:
            #pass
            espines_Grafico.append(np.array(espinesj))
            energiaActual=Energia(espinesj,valorJ)
            lista_Energias.append(energiaActual)
        #espines_Grafico.append(np.array(espinesi))
        
    return lista_Energias

energias= ModeloIsing(10)
fig,ax=plt.subplots(dpi=120)
ax.plot(energias)
ax.set_title("Energía del Modelo 1D con una temperatura ")
ax.set_xlabel("Pasos")
ax.set_ylabel("Energía")
plt.show()

####

valores_de_T=np.linspace(0.1,5,100)
lista_de_E_Promedio=[]
for temp in valores_de_T:
    energias=ModeloIsing(temp)
    print(energias)
    arreglo_energías=np.asarray(energias)
    promedio_Energias=np.sum(arreglo_energías)/len(arreglo_energías)
    lista_de_E_Promedio.append(promedio_Energias)

fig,ax=plt.subplots(dpi=120)
ax.plot(lista_de_E_Promedio)
ax.set_title("Simulación con varias temperaturas del Modelo 1D ")
ax.set_xlabel("$k_bT$")
ax.set_ylabel("Energía")
ax.set_xticklabels(np.arange(-1,6))
plt.show()
"""
