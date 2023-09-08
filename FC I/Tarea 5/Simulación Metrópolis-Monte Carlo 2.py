# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:31:10 2021

@author: Ever Ortega Calderón
"""
import numpy as np
import matplotlib.pyplot as plt

####################################   

#Creación de espines de forma random
def Creacion_espines_alea(numEspines):
    espines=np.random.randint(-1,1,size=numEspines)
    for i in range(numEspines):
        if espines[i]==0:
            if np.random.random()>0.5:
                espines[i]=1
            else:
                espines[i]=-1
    return espines
#####################################

def Energia_Ising(arreglo, valorJ):
    valorEnergia=0
    for i in range (len(arreglo)-1):
        valorEnergia+=arreglo[i]*arreglo[i+1]
    return -valorJ*valorEnergia

#########################################
def Magnetizacion(arreglo_Espines):
    magnetico=0
    for i in arreglo_Espines:
        magnetico+=i
    return magnetico


#### Parámetros de la simulación

kBoltzman=1
temperatura=1
nEspines=100
nPasos=2000
valorJ=1

#Determinación del arreglo:
#Arreglo de espines hacia arriba
#arregloEspines=np.ones([nEspines],np.int)

#Arreglo de espines hacia abajo
#arregloEspines=np.ones([nEspines],np.int)*-1

#Arreglo de espines aleatorios
arregloEspines=Creacion_espines_alea(nEspines)

energia=Energia_Ising(arregloEspines,valorJ)

#Ciclo principal:
    
listaGrafico=[]
listaGrafico.append(np.array(arregloEspines))
energia_acumulada=[Energia_Ising(arregloEspines,valorJ)]
magnetizacion_acumulada=[Magnetizacion(arregloEspines)]
energias_sumadas=0

for k in range(nPasos):
    #Energía del estado
    iEnergia=Energia_Ising(arregloEspines,valorJ)
    #Se escoje el espín a cambiar
    iEspin=np.random.randint(nEspines)
    #Se cambia el estado del espín:
    arregloEspines[iEspin]*=-1
    #Se calcula la energía del posible estado j:
    jEnergia=Energia_Ising(arregloEspines,valorJ)
    #Se calcula el delta E
    deltaE=jEnergia-iEnergia
    #Se calcula la probabilidad de aceptación
    pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
    #Se prueba si se acepta el cambio
    if deltaE>0:
        if np.random.random()<pAceptacion:
            pass #Se acepta el cambio
        else:
            arregloEspines[iEspin]*=-1 #Se rechaza el cambio
    else:
        pass
    listaGrafico.append(np.array(arregloEspines))
    #calculo de energia para cada configuración
    energia_acumulada.append(Energia_Ising(arregloEspines,valorJ))
    #calculo de magnetizacion para cada configuración
    magnetizacion_acumulada.append(Magnetizacion(arregloEspines))
    """
    for i in energia_acumulada:
        energias_sumadas+=i
        energia_interna=energias_sumadas/len(energia_acumulada)
    if np.abs((energia_interna-Energia_Ising(arregloEspines, valorJ)))>umbral:
        pass 
    else:
        print("Ya no vamos para ningún lado, el sistema está en equilibrio")
        break
    """   
for i in energia_acumulada:
        energias_sumadas+=i
        energia_interna=energias_sumadas/len(energia_acumulada)  
        
#Fin del ciclo principal
arregloGrafico=np.asarray(listaGrafico)
 



#Gráfico
fig,ax=plt.subplots(figsize=(10,10),dpi=120)
ax.imshow(arregloGrafico.T,"plasma")
ax.set_title("Simulación del modelo de Ising I-D")
ax.set_xlabel("Pasos")
ax.set_ylabel("Espines")
ax.set_aspect("5")
plt.show()

#print(energia_acumulada)
#print(magnetizacion_acumulada)            
print("Energía en equilibrio con 1 iteración: ", energia_acumulada[-1])   
print("Magnetización en equilibrio con 1 iteración:", magnetizacion_acumulada[-1])       
print("Energía interna U en equilibrio con 1 iteración::", energia_interna)  


############QUE SE HAGA VARIAS VECES
energias_varias_veces=0
magnetizacion_varias_veces=0
repeticiones=100
energias_internas_varias_veces=0
for h in range(0,repeticiones):
    
    
    #Ciclo principal:
    #Determinación del arreglo:
    #Arreglo de espines hacia arriba
    #arregloEspines=np.ones([nEspines],np.int)
    
    #Arreglo de espines hacia abajo
    #arregloEspines=np.ones([nEspines],np.int)*-1
    
    #Arreglo de espines aleatorios
    arregloEspines=Creacion_espines_alea(nEspines)
    
    listaGrafico=[]
    listaGrafico.append(np.array(arregloEspines))
    energia_acumulada=[Energia_Ising(arregloEspines,valorJ)]
    magnetizacion_acumulada=[Magnetizacion(arregloEspines)]
    energias_sumadas=0
    #umbral=5
    for k in range(nPasos):
        #Energía del estado
        iEnergia=Energia_Ising(arregloEspines,valorJ)
        #Se escoje el espín a cambiar
        iEspin=np.random.randint(nEspines)
        #Se cambia el estado del espín:
        arregloEspines[iEspin]*=-1
        #Se calcula la energía del posible estado j:
        jEnergia=Energia_Ising(arregloEspines,valorJ)
        #Se calcula el delta E
        deltaE=jEnergia-iEnergia
        #Se calcula la probabilidad de aceptación
        pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
        #Se prueba si se acepta el cambio
        if deltaE>0:
            if np.random.random()<pAceptacion:
                pass #Se acepta el cambio
            else:
                arregloEspines[iEspin]*=-1 #Se rechaza el cambio
        else:
            pass
        listaGrafico.append(np.array(arregloEspines))
        #calculo de energia para cada configuración
        energia_acumulada.append(Energia_Ising(arregloEspines,valorJ))
        #calculo de magnetizacion para cada configuración
        magnetizacion_acumulada.append(Magnetizacion(arregloEspines))
    energias_varias_veces+=energia_acumulada[-1] 
    #print(energia_acumulada[-1])
    magnetizacion_varias_veces+=magnetizacion_acumulada[-1]
    for i in energia_acumulada:
        energias_sumadas+=i
        energia_interna=energias_sumadas/len(energia_acumulada)  
    energias_internas_varias_veces+=energia_interna

prom_energia=energias_varias_veces/repeticiones
prom_magnetizacion=magnetizacion_varias_veces/repeticiones
prom_energia_interna=energias_internas_varias_veces/repeticiones
print("El promedio de las energías después de: ",repeticiones, " repeticiones, es: ", prom_energia)
print("El promedio de las magnetizaciones después de: ",repeticiones, " repeticiones es: ", prom_magnetizacion)
print("El promedio de las energías internas después de: ",repeticiones, " repeticiones, es: ", prom_energia_interna) 

##Parte E 

#### Parámetros de la simulación
kBoltzman_temperatura=0.0000001
grafico_kbt=[]
grafico_U=[]
grafico_magnetizacion=[]
while kBoltzman_temperatura<=5:
    
    nEspines=100
    nPasos=2000
    valorJ=1
    
    #Determinación del arreglo:
    #Arreglo de espines hacia arriba
    #arregloEspines=np.ones([nEspines],np.int)
    
    #Arreglo de espines hacia abajo
    #arregloEspines=np.ones([nEspines],np.int)*-1
    
    #Arreglo de espines aleatorios
    arregloEspines=Creacion_espines_alea(nEspines)
    
    energia=Energia_Ising(arregloEspines,valorJ)
    
    #Ciclo principal:
        
    listaGrafico=[]
    listaGrafico.append(np.array(arregloEspines))
    energia_acumulada=[Energia_Ising(arregloEspines,valorJ)]
    magnetizacion_acumulada=[Magnetizacion(arregloEspines)]
    energias_sumadas=0
    #umbral=5
    for k in range(nPasos):
        #Energía del estado
        iEnergia=Energia_Ising(arregloEspines,valorJ)
        #Se escoje el espín a cambiar
        iEspin=np.random.randint(nEspines)
        #Se cambia el estado del espín:
        arregloEspines[iEspin]*=-1
        #Se calcula la energía del posible estado j:
        jEnergia=Energia_Ising(arregloEspines,valorJ)
        #Se calcula el delta E
        deltaE=jEnergia-iEnergia
        #Se calcula la probabilidad de aceptación
        pAceptacion=np.exp(-deltaE/(kBoltzman_temperatura))
        #Se prueba si se acepta el cambio
        if deltaE>0:
            if np.random.random()<pAceptacion:
                pass #Se acepta el cambio
            else:
                arregloEspines[iEspin]*=-1 #Se rechaza el cambio
        else:
            pass
        listaGrafico.append(np.array(arregloEspines))
        #calculo de energia para cada configuración
        energia_acumulada.append(Energia_Ising(arregloEspines,valorJ))
        #calculo de magnetizacion para cada configuración
        magnetizacion_acumulada.append(Magnetizacion(arregloEspines))
        """
        for i in energia_acumulada:
            energias_sumadas+=i
            energia_interna=energias_sumadas/len(energia_acumulada)
        if np.abs((energia_interna-Energia_Ising(arregloEspines, valorJ)))>umbral:
            pass 
        else:
            print("Ya no vamos para ningún lado, el sistema está en equilibrio")
            break
        """   
    for i in energia_acumulada:
            energias_sumadas+=i
            energia_interna=energias_sumadas/len(energia_acumulada)  
            
    #Fin del ciclo principal
    #arregloGrafico=np.asarray(listaGrafico)
    grafico_magnetizacion.append(magnetizacion_acumulada[-1])
    grafico_U.append(energia_interna)
    grafico_kbt.append(kBoltzman_temperatura)
    kBoltzman_temperatura+=0.01
    
#Gráfico kbt vs U

fig, ax = plt.subplots(dpi=120)
ax.plot(grafico_kbt,grafico_U)
ax.set_title('Kbt vs U')
ax.set_xlabel('Kbt')
ax.set_ylabel('U')
plt.show()
#Gráfico Kbt vs Magnetización 
fig, ax = plt.subplots(dpi=120)
ax.plot(grafico_kbt,grafico_magnetizacion)
ax.set_title('Kbt vs Magnetización')
ax.set_xlabel('Kbt')
ax.set_ylabel('Magnetización')
plt.show()


###################Parte de g
#### Parámetros de la simulación
kBoltzman_temperatura=0.0000001
grafico_kbt=[]
grafico_U=[]
grafico_magnetizacion=[]
U_2=0
energias_al_cuadrado=0
grafico_calor_especifico=[]
while kBoltzman_temperatura<=5:
    energias_varias_veces=0
    magnetizacion_varias_veces=0
    repeticiones=100
    energias_internas_varias_veces=0
    calor_especifico=0
    for h in range(0,repeticiones):
        
        
        #Ciclo principal:
        #Determinación del arreglo:
        #Arreglo de espines hacia arriba
        #arregloEspines=np.ones([nEspines],np.int)
        
        #Arreglo de espines hacia abajo
        #arregloEspines=np.ones([nEspines],np.int)*-1
        
        #Arreglo de espines aleatorios
        arregloEspines=Creacion_espines_alea(nEspines)
        
        listaGrafico=[]
        listaGrafico.append(np.array(arregloEspines))
        energia_acumulada=[Energia_Ising(arregloEspines,valorJ)]
        magnetizacion_acumulada=[Magnetizacion(arregloEspines)]
        energias_sumadas=0
        #umbral=5
        for k in range(nPasos):
            #Energía del estado
            iEnergia=Energia_Ising(arregloEspines,valorJ)
            #Se escoje el espín a cambiar
            iEspin=np.random.randint(nEspines)
            #Se cambia el estado del espín:
            arregloEspines[iEspin]*=-1
            #Se calcula la energía del posible estado j:
            jEnergia=Energia_Ising(arregloEspines,valorJ)
            #Se calcula el delta E
            deltaE=jEnergia-iEnergia
            #Se calcula la probabilidad de aceptación
            pAceptacion=np.exp(-deltaE/(kBoltzman*temperatura))
            #Se prueba si se acepta el cambio
            if deltaE>0:
                if np.random.random()<pAceptacion:
                    pass #Se acepta el cambio
                else:
                    arregloEspines[iEspin]*=-1 #Se rechaza el cambio
            else:
                pass
            listaGrafico.append(np.array(arregloEspines))
            #calculo de energia para cada configuración
            energia_acumulada.append(Energia_Ising(arregloEspines,valorJ))
            #calculo de magnetizacion para cada configuración
            magnetizacion_acumulada.append(Magnetizacion(arregloEspines))
        energias_varias_veces+=energia_acumulada[-1] 
        #print(energia_acumulada[-1])
        energias_al_cuadrado+=((energia_acumulada[-1])**2 )
        magnetizacion_varias_veces+=magnetizacion_acumulada[-1]
        for i in energia_acumulada:
            energias_sumadas+=i
            energia_interna=energias_sumadas/len(energia_acumulada)  
        energias_internas_varias_veces+=energia_interna
    
    prom_energia=energias_varias_veces/repeticiones
    prom_magnetizacion=magnetizacion_varias_veces/repeticiones
    prom_energia_interna=energias_internas_varias_veces/repeticiones
    U_2=(1/repeticiones)*energias_al_cuadrado
    calor_especifico=(1/(nEspines**2))*((U_2-(prom_energia_interna)**2)/(kBoltzman_temperatura**2))
    grafico_calor_especifico.append(calor_especifico)
    grafico_kbt.append(kBoltzman_temperatura)
    kBoltzman_temperatura+=0.5
    #print("El promedio de las energías después de: ",repeticiones, " repeticiones, es: ", prom_energia)
    #print("El promedio de las magnetizaciones después de: ",repeticiones, " repeticiones es: ", prom_magnetizacion)
    #print("El promedio de las energías internas después de: ",repeticiones, " repeticiones, es: ", prom_energia_interna) 


#Gráfico calor específico vs Magnetización 
fig, ax = plt.subplots(dpi=120)
ax.plot(grafico_kbt,grafico_calor_especifico)
ax.set_title('Kbt vs calor específico')
ax.set_xlabel('Kbt')
ax.set_ylabel('Calor específico')
plt.show()