"""
Tecnológico de Costa Rica
Ever Ortega Calderón
Luis Guerrero
Termodinámica I
Simulación de crema en una taza de café y cálculo de su entropía
"""
import random 
import math
from matplotlib import pyplot as plt  
matriz=[]
#Estas variables dan la dimensión de la matriz cuadrada, que simula la taza de cafe f=filas c=columnas
f=100
c=100
#Número de repeticiones de la simulación
n=20000
#Esta variable permite llevar control sobre la cantidad de simulaciones o pasos en el tiempo
iteraciones=0
#esta función crea la matriz inicial, además de el cambio en cada iteración
#acá se llaman las demás funciones, debido a que en esta parte se dispersan las partículas de crema
def crearmatriz(matriz,f,c,n,iteraciones):
    entropias=[]
    unos=[]
    for i in range (f):
        unos.append(0)
    for i in range (f):
        matriz.append([])
        for j in range(f):
            matriz[i].append(0)
    
    for i in range(10):
        for j in range(10):
            matriz[45+i][45+j]=1
    archi=open("archivo.txt","w") 
    
    for b in range(n):
        
        
        calculo_entropia(entropias,matriz,unos,iteraciones)
        #print(iteraciones)
        iteraciones+=1  
        for a in range(len(matriz)):
            archi.write(str(matriz[a]))
            
            
        archi.write(";")
        for i in range (f):
            for j in range(f):
                #superior izquierda
                if j==0 and i==0:
                    aleatorio=random.randint (1,2)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    else:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
                #superior derecha
                elif j==99 and i==0:
                    aleatorio=random.randint (1,2)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    else:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
                #inferior izquierda
                elif j==0 and i==99:
                    aleatorio=random.randint (1,2)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    else:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                #inferior derecha
                elif j==99 and i==99:
                    aleatorio=random.randint (1,2)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    else:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                #barra central
                elif 0<i<99 and 0<j<99:
                    aleatorio=random.randint (1,4)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    elif aleatorio==2:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    elif aleatorio==3:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                    elif aleatorio==4:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
                # barra superior
                elif i==0 and 0<j<99:
                    aleatorio=random.randint (1,3)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    elif aleatorio==2:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    elif aleatorio==3:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
                #barra inferior
                elif i==99 and 0<j<99:
                    aleatorio=random.randint (1,3)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    elif aleatorio==2:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    elif aleatorio==3:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                #barra lateral izquierda
                elif j==0 and 0<i<99:
                    aleatorio=random.randint (1,3)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j+1]==0:
                            matriz[i][j]=0
                            matriz[i][j+1]=1
                    elif aleatorio==2:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                    elif aleatorio==3:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
                #barra lateral derecha
                elif j==99 and 0<i<99:
                    aleatorio=random.randint (1,3)
                    if aleatorio==1:
                        if matriz[i][j]==1 and matriz[i][j-1]==0:
                            matriz[i][j]=0
                            matriz[i][j-1]=1
                    elif aleatorio==2:
                        if matriz[i][j]==1 and matriz[i-1][j]==0:
                            matriz[i][j]=0
                            matriz[i-1][j]=1
                    elif aleatorio==3:
                        if matriz[i][j]==1 and matriz[i+1][j]==0:
                            matriz[i][j]=0
                            matriz[i+1][j]=1
    grafico(entropias)  
    archi.close()   
    return entropias

#Esta función calcula la entropía para  una iteración
def calculo_entropia(entropias,matriz,unos,iteraciones):
    inicio_fila=0
    final_fila=inicio_fila+10
    contador=0
    parcial_unos=[]
    while contador!=10:
        inicio_columna=0
        final_columna=inicio_columna+10
        contador2=0
        while contador2!=10:
            cantidad_unos=0
            for a in range(inicio_fila,final_fila):
                for b in range (inicio_columna,final_columna):
                    if matriz[a][b]==1:
                        cantidad_unos+=1
            parcial_unos.append(cantidad_unos)
            
            inicio_columna+=10
            final_columna=inicio_columna+10
            contador2+=1
        inicio_fila+=10
        final_fila=inicio_fila+10
        contador+=1
    dispersion (parcial_unos,matriz,iteraciones)
    if iteraciones==0:
        unos=parcial_unos
    else:
        #print(parcial_unos)
        for i in range(0,100):
            nueva= unos[i] +parcial_unos[i]
            unos[i]=nueva
    entropia=0
    for c in unos:
        if c!=0:
            if iteraciones!=0:
                equis=(iteraciones+1)*100
                proba=c/equis
                esta=proba*math.log(proba)
                entropia=entropia + esta
            else:
               proba=c/(100)
               esta=proba*math.log(proba)
               entropia=entropia + esta 
    
    entropias.append(-entropia)
    return entropias    
#Esta función gráfica el estado para los diferentes pasos
def dispersion (parcial_unos, matriz,iteraciones):
    if iteraciones==0:
        x=[]
        y=[]
        for i in range(0,100):
            for j in range(0,100):
                if matriz[i][j]==1:
                    x.append(i)
                    y.append(j)
                else:
                    pass
        fig, ever= plt.subplots()    
        plt.ion()
        
        ever.plot(x,y,'ro')
        plt.title("Paso 0",
                  fontsize=20)
        plt.xlabel("columnas",
                   fontsize=20,)
        plt.ylabel("filas",
                   fontsize=20)
        plt.ylim(0,100)
        plt.xlim(0,100)
    if iteraciones==9:
        x=[]
        y=[]
        for i in range(0,100):
            for j in range(0,100):
                if matriz[i][j]==1:
                    x.append(i)
                    y.append(j)
                else:
                    pass
        fig, ever= plt.subplots()    
        plt.ion()
        
        ever.plot(x,y,'ro')
        plt.title("Paso 10",
                  fontsize=20)
        plt.xlabel("columnas",
                   fontsize=20,)
        plt.ylabel("filas",
                   fontsize=20)
        plt.ylim(0,100)
        plt.xlim(0,100)
    
    if iteraciones==99:
        x=[]
        y=[]
        for i in range(0,100):
            for j in range(0,100):
                if matriz[i][j]==1:
                    x.append(i)
                    y.append(j)
                else:
                    pass
        fig, ever= plt.subplots()    
        plt.ion()
        
        ever.plot(x,y,'ro')
        plt.title("Paso 100",
                  fontsize=20)
        plt.xlabel("columnas",
                   fontsize=20,)
        plt.ylabel("filas",
                   fontsize=20)
        plt.ylim(0,100)
        plt.xlim(0,100)
    if iteraciones==999:
        x=[]
        y=[]
        for i in range(0,100):
            for j in range(0,100):
                if matriz[i][j]==1:
                    x.append(i)
                    y.append(j)
                else:
                    pass
        fig, ever= plt.subplots()    
        plt.ion()
        
        ever.plot(x,y,'ro')
        plt.title("Paso 1000",
                  fontsize=20)
        plt.xlabel("columnas",
                   fontsize=20,)
        plt.ylabel("filas",
                   fontsize=20)
        plt.ylim(0,100)
        plt.xlim(0,100)
    if iteraciones==9999:
        x=[]
        y=[]
        for i in range(0,100):
            for j in range(0,100):
                if matriz[i][j]==1:
                    x.append(i)
                    y.append(j)
                else:
                    pass
        fig, ever= plt.subplots()    
        plt.ion()
        
        ever.plot(x,y,'ro')
        plt.title("Paso 10000",
                  fontsize=20)
        plt.xlabel("columnas",
                   fontsize=20,)
        plt.ylabel("filas",
                   fontsize=20)
        plt.ylim(0,100)
        plt.xlim(0,100)
        
#Esta función obtiene el gráfico de entropía
        
def grafico(entropias):
    datos_pasos=[]
    iteracion=1
    
    for i in entropias:
        datos_pasos.append(iteracion)
        iteracion+=1
    plt.ion()
    fig2,ever2=plt.subplots()
    
    ever2.plot(datos_pasos,entropias)
    plt.title("Evolución de la entropía del sistema",
              fontsize=20)
    plt.ylabel("entropía",
               fontsize=20)
    plt.xlabel("tiempo (pasos)",
               fontsize=20)

print(crearmatriz(matriz,f,c,n,iteraciones))
