# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 02:36:57 2021

@author: Ever Ortega Calderón
"""
#Se importan las librerias pertinentes
import numpy as np
import matplotlib.pyplot as plt
#import random
                               
"""
Se crea la función DecodificacionCromosoma encarga de decodificar un cromosoma, del número de la ciudad a las coordenadas de la misma
Recibe:
    cromosoma: el cromosoma a decodificar    
Retorna:
    distancia:el valor de distancia que hay entre las ciudades que contienen el cromosoma
"""
def DecodificacionCromosoma(cromosoma):
    distancia=0
    lista_x=[]
    lista_y=[]
    #Este ciclo se emplea para almacenar en las listas los valores de posición de x y de y según se deba
    for i in range(len(cromosoma)):
        posicion=int(cromosoma[i])
        coordenada_x=listaCoordenadas[posicion][0]
        coordenada_y=listaCoordenadas[posicion][1]
        lista_x.append(coordenada_x)
        lista_y.append(coordenada_y)
    
    nGenes=len(cromosoma)
        #Este ciclo calcula la ditancia euclidiana y la almacena

    for j in range(0,nGenes-1):
        deltaX=lista_x[j]-lista_x[j+1]
        deltaY=lista_y[j]-lista_y[j+1]
        distancia+=np.sqrt(deltaX**2+deltaY**2)
    #Se calcula la distancia entre el punto inicial para que así la trayectoria sea cerrada

    deltaX_i=lista_x[nGenes-1]-lista_x[0]
    deltaY_i=lista_y[nGenes-1]-lista_y[0]
    distancia_i=np.sqrt(deltaX_i**2+deltaY_i**2)
    distancia+=distancia_i
    return distancia
"""
Se crea la función InicializacionModificada encargada de generar una población inicial de forma que el siguiente sea el vecino más cercano
en la cual los cromosomas tienen una codificación de 0 a la cantidad de ciudades 
Recibe:
    tamañoPoblacion: cantidad de cromosomas deseados en la población
    nGenes:cantidad de elementos por cromosoma 
Retorna:
    poblacion: matriz 'tamaño población x nGenes' que representa la población inicial
"""
def InicializacionModificada(tamañoPoblacion,nGenes):
    #Se inicializa la matriz poblacion que contendrá los cromosomas
    poblacion=np.zeros((tamañoPoblacion, nGenes))
    
    #Este ciclo crea la población, añadiendo un cromosoma por iteración hasta completar el tamaño deseado
    for i in range(tamañoPoblacion):
        #Se designa un nodo inicial de forma aleatoria 
        nodo_inicial=np.random.randint(0,nGenes)
        #Se crea la lista que almacenará los genes por cromosoma creado, para revisar que no se repitan nodos
        lista_Ciudades = [nodo_inicial]
        #Este ciclo crea un cromosoma, al añadir la cantidad de genes deseada
        for j in range(nGenes):
            mejor_ruta=np.exp(100)
            #Este ciclo revisa todas las ciudades disponibles cuál es el vecino más cercano
            for k in range(nGenes):
                if k not in lista_Ciudades:
                    ruta_actual=DecodificacionCromosoma([lista_Ciudades[-1],k])
                    if ruta_actual<mejor_ruta:
                        mejor_ruta=ruta_actual
                        vecino_mas_cercano=k
            lista_Ciudades.append(vecino_mas_cercano)
            poblacion[i,j]=vecino_mas_cercano
    return poblacion
"""
Se crea la función EvaluarIndividuo que es la encarga de calcular el valor de ajuste para una distancia
Recibe:
    distancia_euclideana: valor de distancia
    
Retorna:
    valorF:valor de ajuste, inverso de la distancia_euclideana
"""
def EvaluarIndividuo(distancia_euclideana):
    """
    Toma como entrada el arreglo de variables reales a evaluar en la función de ajuste
    Retorna el valor de la función evaluada en los valores de entrada
    """
    ValorF = 1/distancia_euclideana
    
    return ValorF
"""
Se crea la función  OperadorMutacion encargada de mutar un cromosoma
Recibe:
    cromosoma:cromosoma a mutar
    p_mut:probabilidad de que suceda la mutación
    
Retorna: 
    cromosomaMutado:cromosoma producto de la mutación    
"""
def OperadorMutacion(cromosoma, p_mut):
    """
    Escriba una función que realice la mutación de un cromosoma con probabilidad p_mut
    """
    nGenes = len(cromosoma)
    
    cromosomaMutado = np.copy(cromosoma)

    # Analice la implementación del operador mutación
    
    nAleatorio = np.random.random()
    Pos1 = np.random.randint(0,nGenes)
    Pos2 = np.random.randint(0,nGenes)
    #Con este if se asegura que no se mute el primer gen del cromosoma
    if Pos1!=0 and Pos2!=0:
        if nAleatorio < p_mut:
            cromosomaMutado[Pos1] = cromosoma[Pos2]
            cromosomaMutado[Pos2] = cromosoma[Pos1]

    return cromosomaMutado

"""
Se crea la función Encontrar_cromosoma_optimo encargada de ubicar entre toda la población
todos los valores de ajuste
Recibe:
    poblacion: todos los cromosomas para esta poblacion
    tamañoPoblacion: cantidad de cromosomas deseados en la población
    nGenes:cantidad de elementos por cromosoma 
Retorna:
    valores_ajuste:lista con los valores de ajuste para cada cromosoma
"""

def Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes):
    valores_ajuste=[]
    #Ciclo que calcula los ajustes recorriendo cada cromosoma
    for i in range(tamañoPoblacion):
        cromosoma=poblacion[i]
        distancia_cromosoma_i=DecodificacionCromosoma(cromosoma)
        valor_ajus=EvaluarIndividuo(distancia_cromosoma_i)
        valores_ajuste.append(valor_ajus)
    """
    ajuste_max=np.max(valores_ajuste)
    for j in range(valores_ajuste):
        if valores_ajuste[j]==ajuste_max:
            posicion_ajuste_max=j
    mejor_cromosoma=poblacion[posicion_ajuste_max]
    """
    return valores_ajuste

"""
Se crea la función LeerArchivoConCorchetes encargada de leer el archivo en caso de que tenga
corchetes y comas, tal cómo lo muestra python
Recibe:
    nombre_archivo_txt: nombre del archivo deseado a leer
    
Retorna:
    listaCoordenadas: contiene los valores de las coordenadas de las ciudades
"""

#SI EL TXT TIENE CORCHETES, LEER ESTO:
def LeerArchivoConCorchetes(nombre_archivo_txt):
    archivo=open(nombre_archivo_txt,"r")
    mensaje=archivo.read()
    archivo.close
    
    eliminar="[]"
    for i in range(len(eliminar)):
        mensaje=mensaje.replace(eliminar[i],"")   
    
    mensaje=mensaje.split(",")
    listaCoordenadas=[]
    for i in range(0,len(mensaje),2):
        agregar_coord=[]
        agregar_coord.append(float(mensaje[i]))
        agregar_coord.append(float(mensaje[i+1]))
        listaCoordenadas.append(agregar_coord)
    return listaCoordenadas

#SI EL TXT SOLO ESTÁ SEPARADO POR ESPACIO, LEER ESTO.
"""
Se crea la función LeerArchivoSeparadoPorEspacios que lee el archivo en caso de que
la separación entre una coordenada x y una y sea solo espacio
Recibe:
    nombre_archivo_txt: nombre del archivo deseado a leer  
  
Retorna:
    listaCoordenadas: contiene los valores de las coordenadas de las ciudades

"""
def LeerArchivoSeparadoPorEspacios(nombre_archivo_txt):
    listaCoordenadas=np.loadtxt(nombre_archivo_txt,dtype=float)
    return listaCoordenadas
 

#Código principal    
#Se cargan las coordenadas de las ciudades   
listaCoordenadas=LeerArchivoConCorchetes("CoordenadasCiudades.txt")
#Se definen valores iniciales
nGenes=len(listaCoordenadas)
tamañoPoblacion=200
nGeneraciones=2000
p_mut=0.27

#Se inicializa la población
poblacion = InicializacionModificada(tamañoPoblacion, nGenes)



lista_valores_ajuste=[]
poblaciones=[]
#Valores de ajustes y poblaciones de todas las generaciones, se agregan a una lista cada una
for i in range(nGeneraciones):
    lista_valores_ajuste.append(Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes))
    poblaciones.append(poblacion)
    #Se calcula random cuantas mutaciones se harán en un rango de 3 a 10
    cantidad_de_mutaciones=np.random.randint(3,10)
    #Se mutan todos los genes para así tener la siguiente generación la cantidad de veces predicha
    for k in range(3,cantidad_de_mutaciones):
        for j in range (tamañoPoblacion):
            cromosoma_a_mutar=poblacion[j]
            poblacion[j]=OperadorMutacion(cromosoma_a_mutar,p_mut)
        
mejor_valor_ajuste=np.max(lista_valores_ajuste[0])
generacion_con_mejor_ajuste=0
#Reviso la posición del mejor cromosoma, el que tiene el mejro ajuste, en la población
for j in range (0,len(lista_valores_ajuste[0])):
    if lista_valores_ajuste[0][j]==np.max(lista_valores_ajuste[0]):
        mejor_cromosoma_de_todos=poblaciones[i][j]
#Reviso cual generacion tiene el mejor valor de ajuste de entre todos
for i in range(1,len(lista_valores_ajuste)):
    #Si hay un valor de ajuste más alto entonces se redefine este cómo el mejor valor de ajuste
    if mejor_valor_ajuste<np.max(lista_valores_ajuste[i]):
        mejor_valor_ajuste=np.max(lista_valores_ajuste[i])
        generacion_con_mejor_ajuste=i
        #Reviso la posición del mejor cromosoma, el que tiene el mejro ajuste, en la población
        for j in range (0,len(lista_valores_ajuste[i])):
            if lista_valores_ajuste[0][j]==np.max(lista_valores_ajuste[i]):
                mejor_cromosoma_de_todos=poblaciones[i][j]
    else:
        pass
#Se imprime el mejor valor de ajuste y el cromosoma más óptimo      
print("Mejor valor de ajuste: ", mejor_valor_ajuste)
print("Distancia más corta: ", 1/mejor_valor_ajuste)
print("Cromosoma óptimo: ", mejor_cromosoma_de_todos)

#Universo de puntos de las generaciones
generaciones_grafico=np.arange(0,nGeneraciones)

#Creación de lista de valores max y promedios para gráfico
valores_max_grafico=[]
valores_prom_grafico=[]
for i in lista_valores_ajuste:
    valores_max_grafico.append(np.max(i))
    valores_prom_grafico.append(np.mean(i))
#Se grafica los valores de ajuste promedio y máximo para cada generación
fig,ax=plt.subplots(dpi=120)
ax.plot(generaciones_grafico,valores_max_grafico,"b")
ax.plot(generaciones_grafico,valores_prom_grafico, "r")
ax.set_title('PVA valores ajuste generaciones, algotirmo modificado')
ax.set_xlabel('Generaciones')
ax.set_ylabel('Valores')
ax.legend(["Valores máximos","Valores promedio"])
plt.show()


#Graficar mejor cromosoma
coordenadas_mejor_cromosoma=[]
coordenadas_mejor_cromosoma_x=[]
coordenadas_mejor_cromosoma_y=[]
for i in mejor_cromosoma_de_todos:
    coordenadas_mejor_cromosoma.append(listaCoordenadas[int(i)])
for j in range(len(coordenadas_mejor_cromosoma)):
    coordenadas_mejor_cromosoma_x.append(coordenadas_mejor_cromosoma[j][0])
    coordenadas_mejor_cromosoma_y.append(coordenadas_mejor_cromosoma[j][1])
#Se agrega coordenada para que el camino sea cerrado
coordenadas_mejor_cromosoma.append(coordenadas_mejor_cromosoma[0])
coordenadas_mejor_cromosoma_x.append(coordenadas_mejor_cromosoma_x[0])
coordenadas_mejor_cromosoma_y.append(coordenadas_mejor_cromosoma_y[0])
#Se guarda el cromosoma más óptimo en un txt
np.savetxt('caminoMásCorto_AGE, algotirmo modificado.txt',coordenadas_mejor_cromosoma)
#Se grafica la ruta del cromosoma óptimo     
fig,ax=plt.subplots(dpi=120)
ax.plot(coordenadas_mejor_cromosoma_x,coordenadas_mejor_cromosoma_y, "c-")
ax.plot(coordenadas_mejor_cromosoma_x,coordenadas_mejor_cromosoma_y, "ro")
ax.set_title('Mejor ruta, algotirmo modificado')
ax.set_xlabel('Coordenada x')
ax.set_ylabel('Coordenada y')
ax.legend(["Ruta","Ubicación"])
plt.show()    
    
  

    
    