# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:08:15 2021

@author: Ever Ortega Calderón
"""
import numpy as np
import matplotlib.pyplot as plt

#Función Creacion_espines_alea que crea una configuración de espines de forma aleatoria
#Recibe la cantidad de espines deseada y retorna el arreglo de espines ordenado de forma aleatoria
def Creacion_espines_alea(numEspines):
    espines=np.random.randint(-1,1,size=numEspines)
    for i in range(numEspines):
        if espines[i]==0:
            if np.random.random()>0.5:
                espines[i]=1
            else:
                espines[i]=-1
    return espines
##Función Energia_Ising que calcula la energía de la configuración 
#Recibe el arreglo al que le debe calcular la energía y el valor de la constante J
#Retorna el valor de la energía para esa configuración de espines
def Energia_Ising(arreglo, valorJ):
    valorEnergia=0
    for i in range (len(arreglo)-1):
        valorEnergia+=arreglo[i]*arreglo[i+1]
    return -valorJ*valorEnergia

#Función Magnetizacion que calcula la magnetización de la configuración 
#Recibe el arreglo al que le debe calcular la magnetización 
#Retorna el valor de la magnetización para esa configuración de espines
def Magnetizacion(arreglo_Espines):
    magnetico=0
    for i in arreglo_Espines:
        magnetico+=i
    return magnetico

"""
Función Intercambio_Espines que ejecuta el intercambio de espines y calcula la energia acumulada de los espines así cómo la magnetización
Recibe:
    listaGrafico: arreglo que acumula las configuraciones de espines para todos los pasos 
    arregloEspines: configuración inicial de espines
    energia_acumulada: arreglo con las energías para todos los pasos, por ende para cada una de las configuraciones
    magnetizacion_acumulada: arreglo con las magnetizaciones para todos los pasos, por ende para cada una de las configuraciones
    kBoltzman_temperatura: el valor de KbT de la configuración
Retorna:
    listaGrafico: arreglo que acumula las configuraciones de espines para todos los pasos 
    energias_prom_equilibrio_una_temperatura_listo: valor de energía en el equilibrio, donde para el equilibrio se cuentan los pasos después de 2000
    magnetizacion_prom_equilibrio_una_temperatura_listo: valor de magnetización en el equilibrio, donde para el equilibrio se cuentan los pasos después de 2000
    energia_acumulada: arreglo con las energías para todos los pasos, por ende para cada una de las configuraciones
    magnetizacion_acumulada: arreglo con las magnetizaciones para todos los pasos, por ende para cada una de las configuraciones
"""
def Intercambio_Espines(listaGrafico, arregloEspines ,energia_acumulada, magnetizacion_acumulada, kBoltzman_temperatura):
    energias_equilibrio_una_temperatura=0
    magnetizacion_equilibrio_una_temperatura=0
    
    #Ciclo for que itera la configuración de espines, modificandola estocasticamente para todos los pasos
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
    #Se establece que se considerará un valor cómo en el cuál después de él se encontrará el equilibrio
    equilibrio=2000
    #Se usa un ciclo para calcular la energía y la magnetización despues del valor de equilibrio
    for i in range(equilibrio,len(energia_acumulada)):
        energias_equilibrio_una_temperatura+=energia_acumulada[i-1]
        magnetizacion_equilibrio_una_temperatura+=magnetizacion_acumulada[i-1]
        
    #Se promedia el valor de energía y magnetización en el equilibrio
    energias_prom_equilibrio_una_temperatura_listo=energias_equilibrio_una_temperatura/(len(energia_acumulada)-2000)
    magnetizacion_prom_equilibrio_una_temperatura_listo=magnetizacion_equilibrio_una_temperatura/(len(magnetizacion_acumulada)-2000)

    return listaGrafico,energias_prom_equilibrio_una_temperatura_listo,magnetizacion_prom_equilibrio_una_temperatura_listo,energia_acumulada,magnetizacion_acumulada

"""
Función Iterar_varias_veces que hace la simulación de la función Intercambio_Espines, para promediar y eliminar fluctuaciones
Recibe:
    listaGrafico:arreglo que acumula las configuraciones de espines para todos los pasos 
    espines_configuracion_inicial: configuración inicial de espines
    listaGrafico_varias_veces: arreglo que acumula las configuraciones de espines para todos los pasos y para todas las veces que se corre para eliminar fluctuaciones
    energias_varias_veces: almacena las energías de todas las corridas que se hacen para eliminar fluctuaciones
    magnetizacion_varias_veces: almacena las magnetizaciones de todas las corridas que se hacen para eliminar fluctuaciones
    repeticiones: cantidad de veces que se corre la simulación para eliminar fluctuaciones
    kBoltzman_temperatura: el valor de KbT de la configuración
    prom_energia: suma de las energias de todas las corridas
    prom_magnetizacion: suma de las magnetizaciones de todas las corridas
    U_2: valor de la constante U_2

Retorna:
    listaGrafico_varias_veces: arreglo que acumula las configuraciones de espines para todos los pasos, así cómo para todas las corridas que se hacen para eliminar fluctuaciones
    almacena las energías de todas las corridas que se hacen para eliminar fluctuaciones
    magnetizacion_varias_veces: almacena las magnetizaciones de todas las corridas que se hacen para eliminar fluctuaciones
    prom_energia_listo: energía promediada con la cantidad de corridas realizadas para eliminar fluctuaciones
    prom_magnetizacion_listo:magnetización promediada con la cantidad de corridas realizadas para eliminar fluctuaciones
    U_2_listo: valor de las energias en el equilibrio al cuadrado, sumadas y dividio entre la cantidad de corridas realizadas para eliminar fluctuaciones
"""
def Iterar_varias_veces(listaGrafico,espines_configuracion_inicial, listaGrafico_varias_veces, energias_varias_veces, magnetizacion_varias_veces,repeticiones,kBoltzman_temperatura,prom_energia,prom_magnetizacion, U_2):
    energias_varias_veces_iter=[]
    magnetizacion_varias_veces_iter=[]
    #Se corren la simulación una cantidad determinada de veces para eliminar fluctuaciones estadisticas
    for h in range(0,repeticiones):
        
        #Se almacena cada una de las variables empleando la función Intercambio _Espines que hace todos los cálculos para una única simulación
        llamada_funcion=Intercambio_Espines(listaGrafico, espines_configuracion_inicial, energias_varias_veces, magnetizacion_varias_veces, kBoltzman_temperatura)
        listaGrafico_varias_veces.append(llamada_funcion[0])
        
        
        energias_varias_veces_iter.append(llamada_funcion[1])
        magnetizacion_varias_veces_iter.append(llamada_funcion[2])
    
    #Se suman a una variable determinada cada una de las variables 
    for i in energias_varias_veces_iter:
        prom_energia+=i
    for i in magnetizacion_varias_veces_iter:
        prom_magnetizacion+=i
    for i in energias_varias_veces_iter:
        U_2+=(i)**2
    #Se promedian las variables con la cantidad de repeticiones que se hacen 
    prom_energia_listo=prom_energia/repeticiones
    prom_magnetizacion_listo=prom_magnetizacion/repeticiones
    
    
    U_2_listo=(1/repeticiones)*U_2
    return listaGrafico_varias_veces, energias_varias_veces_iter, magnetizacion_varias_veces_iter,prom_energia_listo,prom_magnetizacion_listo,U_2_listo
#### Parámetros de la simulación

kBoltzman_temperatura=1
nEspines=100
#Número de pasos debe ser mayor a 2000
#Se solicitan la cantidad de pasos deseados, se cuida que sean más de 2000 para asegurar al sistema en equilibrio  y al interactuar con el usuario se cuidan posibles errores
while True:
    try:
        nPasos=int(input("Digite la cantidad de pasos deseados: "))
        if nPasos==0 or nPasos<=2000:
            print("La cantidad de pasos deseados no puede ser ni cero ni menor a 2000, pues en 2000 se alcanzará el equilibrio, intentelo de nuevo por favor")
        else:
            break
            
    except:
        print("La cantidad de pasos deseados no puede ser ni cero ni menor a 2000, pues en 2000 se alcanzará el equilibrio, intentelo de nuevo por favor")


valorJ=1
energias_equilibrio_una_temperatura=0
magnetizacion_equilibrio_una_temperatura=0
#Determinación del arreglo:
#Variable que indica la configuración de espines usadas, solicitada para el usuario, por ende se cuidan posibles errores que puedan suceder
while True:
    try:
        configuracion_usada=int(input("Digite la configuración inicial que desea, 1 para arreglo de espines hacia arriba, 2 arreglo de espines hacia abajo, 3 para arreglo de espines aleatorios: "))
        if configuracion_usada==1 or configuracion_usada==2 or configuracion_usada==3:
            break
        else:
            print("No puede digitar un número diferente a 1,2 o 3, intente de nuevo por favor")
    except:
        print("No puede digitar un número diferente a 1,2 o 3, intente de nuevo por favor")
#Se establece la configuración inicial según el valor que el usuario digitó   
if configuracion_usada==1:
    #Arreglo de espines hacia arriba, configuración 1
    arregloEspines=np.ones([nEspines],np.int)
elif configuracion_usada==2:
    #Arreglo de espines hacia abajo , configuración 2
    arregloEspines=np.ones([nEspines],np.int)*-1
elif configuracion_usada==3:
    #Arreglo de espines aleatorios, configuración 3
    arregloEspines=Creacion_espines_alea(nEspines)

energia=Energia_Ising(arregloEspines,valorJ)

#Ciclo principal:
    
#Punto b
listaGrafico=[]
listaGrafico.append(np.array(arregloEspines))
energia_acumulada=[Energia_Ising(arregloEspines,valorJ)]
magnetizacion_acumulada=[Magnetizacion(arregloEspines)]
listaGrafico, energias_prom_equilibrio_una_temperatura,magnetizacion_prom_equilibrio_una_temperatura,energias_acumuladas_1iter,magnetizacion_acumulada_1iter=Intercambio_Espines(listaGrafico,arregloEspines, energia_acumulada, magnetizacion_acumulada, kBoltzman_temperatura)
###Grafico de los pasos contra la energía para 1 iteración 
arreglo_pasos=np.linspace(0,nPasos+1,nPasos+1)
fig, ax = plt.subplots(dpi=120)
ax.plot(arreglo_pasos,energia_acumulada)
ax.set_title('Pasos contra energía acumulada para una iteración')
ax.set_xlabel('Pasos')
ax.set_ylabel('Energía')
plt.show()
#Grafico de los pasos contra la magnetización para una iteración 
fig, ax = plt.subplots(dpi=120)
ax.plot(arreglo_pasos,magnetizacion_acumulada)
ax.set_title('Pasos contra magnetización para una iteración')
ax.set_xlabel('Pasos')
ax.set_ylabel('Magnetización')
plt.show()

arregloGrafico=np.asarray(listaGrafico)
#Gráfico de la primera iteración de los espines 
fig,ax=plt.subplots(figsize=(10,10),dpi=120)
ax.imshow(arregloGrafico.T,"plasma")
ax.set_title("Simulación del modelo de Ising I-D")
ax.set_xlabel("Pasos")
ax.set_ylabel("Espines")
ax.set_aspect("5")
plt.show()

           
print("Energía en equilibrio : ", energias_prom_equilibrio_una_temperatura)   
print("Magnetización en equilibrio:", magnetizacion_prom_equilibrio_una_temperatura)       
       
#Parte C
listaGrafico_varias_veces=[]
#listaGrafico_varias_veces.append(listaGrafico)
energias_varias_veces=[]
#energias_varias_veces.append(energias_prom_equilibrio_una_temperatura)
magnetizacion_varias_veces=[]
#magnetizacion_varias_veces.append(magnetizacion_equilibrio_una_temperatura)
repeticiones=50
energias_internas_varias_veces=0
prom_energia=0
prom_magnetizacion=0

U_2=0

listaGrafico_varias_veces, energias_varias_veces, magnetizacion_varias_veces,prom_energia,prom_magnetizacion,U_2=Iterar_varias_veces(listaGrafico,arregloEspines, listaGrafico_varias_veces, energias_varias_veces, magnetizacion_varias_veces,repeticiones,kBoltzman_temperatura,prom_energia,prom_magnetizacion,U_2)
#Se muestra al usuario el resultado de la simulación 
print("El promedio de las energías después de: ",repeticiones, " repeticiones, es: ", prom_energia)
print("El promedio de las magnetizaciones después de: ",repeticiones, " repeticiones es: ", prom_magnetizacion)

#Parte E
#Se corre la simulación para KbT variables
#Valor inicial de KbT
kbt_variable=0.1
#Se establecen listas de almacenamientos
kbt_variable_grafico=[]
energia_interna_grafico=[]
magnetizacion_variable_grafico=[]
#lista_grafico_varias_veces=[]
U_2_variable=[]
calor_especifico_variable=[]
energias_varias_veces=[]

magnetizacion_varias_veces=[]
while kbt_variable<=5:
    U_2=0
    energias_varias_veces=[]
    magnetizacion_varias_veces=[]
    prom_energia=0
    prom_magnetizacion=0
    u_agregar=0
    U_2_variable=0
    asignacion_funcion=Iterar_varias_veces(listaGrafico,arregloEspines, [], energias_varias_veces, magnetizacion_varias_veces,repeticiones,kbt_variable,prom_energia,prom_magnetizacion,U_2)
    u_agregar=asignacion_funcion[3]
    energia_interna_grafico.append(u_agregar)
    kbt_variable_grafico.append(kbt_variable)
    magnetizacion_variable_grafico.append(asignacion_funcion[4])
    U_2_variable=asignacion_funcion[5]
   
    calor_especifico_variable.append((1/(nEspines**2))*((U_2_variable-u_agregar**2)/(kbt_variable**2)))
    kbt_variable+=0.1

#Soluciones analíticas, se calculan para los valores de KbT todas las soluciones análiticas para poder comparar
#Se almacenan los valores de cada variable en un arreglo diferente para posteriormente graficarlos
#En azul solución númerica, en rojo solución númerica 
B=0
analitica_u=[]
analitica_magnetizacion=[]
analitica_calor_especifico=[]
for i in kbt_variable_grafico:
    analitica_u.append(-nEspines*((np.exp(valorJ/i)-np.exp(-valorJ/i))/(np.exp(valorJ/i)+np.exp(-valorJ/i))))
    analitica_magnetizacion.append((nEspines*np.exp(valorJ/i)*np.sinh(B/i))/(np.sqrt(np.exp(2*valorJ/i)*(np.sinh(B/i)**2)+np.exp(-2*valorJ/i))))    
    analitica_calor_especifico.append(((valorJ/i)**2)/((np.cosh(valorJ/i))**2))
#Gráfico kbt vs U
fig,ax=plt.subplots(1,1)
ax.plot(kbt_variable_grafico,energia_interna_grafico,"b")
ax2=ax.twinx()
ax2.plot(kbt_variable_grafico,analitica_u, "r")
ax.set_title('Kbt vs U')
ax.set_xlabel('Kbt')
ax.set_ylabel('U Númerica',color="b")
ax2.set_ylabel('U Analítica',color="r")
plt.show()

#Gráfico Kbt vs Magnetización 
fig,ax=plt.subplots(1,1)
ax.plot(kbt_variable_grafico, magnetizacion_variable_grafico,color="b")
ax2=ax.twinx()
ax2.plot(kbt_variable_grafico,analitica_magnetizacion, color="r")
ax.set_title('Kbt vs Magnetización')
ax.set_xlabel('Kbt')
ax.set_ylabel('Magnetización Númerica',color="b")
ax2.set_ylabel('Magnetización Analítica',color="r")
plt.show()

#Gráfico calor específico vs KBT
fig,ax=plt.subplots(dpi=120)
ax.plot(kbt_variable_grafico, calor_especifico_variable,"b")
ax2=ax.twinx()
ax2.plot(kbt_variable_grafico,analitica_calor_especifico, "r")
ax.set_title('Kbt vs calor específico')
ax.set_xlabel('Kbt')
ax.set_ylabel('Calor Específico Númerico',color="b")
ax2.set_ylabel('Calor Específico Analítico',color="r")
plt.show()