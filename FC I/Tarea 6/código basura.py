# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 19:04:29 2021

@author: Ever Ortega Calderón
"""

#print(InicializarPoblacion(5,5))
"""
def permutaciones(arreglo_ciudades, end=[]):
    if len(arreglo_ciudades) == 0:
        print(end)
    else:
        for i in range(len(arreglo_ciudades)):
            permutaciones(arreglo_ciudades[:i] + arreglo_ciudades[i+1:], end + arreglo_ciudades[i:i+1])
          
#permutaciones([4,5,6,2])

def CodificacionDeCromosomas(cant_ciudades):
    ciudades=list(range(cant_ciudades))
    #ciudades_permutadas=permutations(ciudades)
    """
    #if ciudades_permutadas[0][0]==ciudades_permutadas[-1][-1]:
    #    pass
    #else:
    #    CodificacionDeCromosomas(cant_ciudades)
        
    """
    poblacion=permutaciones(ciudades)
    return poblacion
    
print(CodificacionDeCromosomas(4))
"""    

listaCoordenadas=[]
archivo=open("CoordenadasCiudades.txt","r")
for linea in archivo:
    listaCoordenadas.append(np.array(linea))
archivo.close


archivo=open("CoordenadasCiudades.txt","r")
mensaje=archivo.read()
archivo.close
listaCoordenadas=np.asarray(mensaje)


""" 
actual_valores_ajuste,mejor_cromosoma_actual=Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes)
#mejor_ajuste_actual=np.max(actual_valores_ajuste)
lista_valores_ajuste.append(actual_valores_ajuste)

mejor_de_todos_cromosomas=mejor_cromosoma_actual
for i in range(1,nGeneraciones):
    
    for j in range (tamañoPoblacion):
        cromosoma=poblacion[j]
        poblacion[j]=OperadorMutación(cromosoma,tamañoPoblacion,nGenes)
    mejor_cromosoma_viejo=mejor_cromosoma_actual  
    #mejor_ajuste_viejo=mejor_ajuste_actual
    actual_valores_ajuste,mejor_cromosoma_actual=Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes)
    
    lista_valores_ajuste.append(actual_valores_ajuste)
    if 
"""   
"""

nGeneraciones=5.
lista_valores_ajuste=[]
lista_valores_maximos=[]
lista_promedios=[]
actual_valores_ajuste,actual_valor_max,actual_posicion_ajuste_max=Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes)
lista_valores_ajuste.append(actual_valores_ajuste)
for i in range(nGeneraciones):
    actual_valores_ajuste,actual_valor_max,actual_posicion_ajuste_max=Encontrar_cromosoma_optimo(poblacion,tamañoPoblacion,nGenes)
    lista_valores_ajuste.append(actual_valores_ajuste)
    print("El valor de la ac")
    for j in range (tamañoPoblacion):
        cromosoma=poblacion[j]
        poblacion[j]=OperadorMutación(cromosoma,tamañoPoblacion,nGenes)
    
"""   
    