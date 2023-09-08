import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def CaminoAleatorio(lista_Pos, nIter):
    """
    Genera un par ordenado aleatorio respecto al punto aanterior
    """
    xPos = (np.random.random()-0.5)*2
    yPos = (np.random.random()-0.5)*2

    nuevaxPos = lista_Pos[0][nIter-1] + xPos/(np.sqrt(xPos**2+yPos**2))
    nuevayPos = lista_Pos[1][nIter-1] + yPos/(np.sqrt(xPos**2+yPos**2))

    lista_Pos[0].append(nuevaxPos)
    lista_Pos[1].append(nuevayPos)

    return lista_Pos


nPasos = 1000


def Caminos(nPasos):
    K=32
    R_result=0
    for i in range(1,K+1):
        camino1=[[0.],[0.]]
        for j in range(1,nPasos):
            camino1=CaminoAleatorio(camino1, j)
            R2=(camino1[-1][0]**2+camino1[-1][1]**2)/nPasos
            R_result+=R2/K
    return R_result,camino1
            
R2,camino=Caminos(nPasos)           

print(R2)

resultado=camino[0][0]*camino[1][1]/R2

print(resultado)


  
fig,ax=plt.subplots(1,1,dpi=150)
ax.plot(camino[0],camino[1], c="m", lw=0.5)
ax.set_title("Caminos aleatorios")
plt.show()

#############################################
#Análisis 3D#

def CaminoAleatorio3D(lista_Pos, nIter):
    """
    Genera un par ordenado aleatorio respecto al punto aanterior
    """
    xPos = (np.random.random()-0.5)*2
    yPos = (np.random.random()-0.5)*2
    zPos = (np.random.random()-0.5)*2

    nuevaxPos = lista_Pos[0][nIter-1] + xPos/(np.sqrt(xPos**2+yPos**2+zPos**2))
    nuevayPos = lista_Pos[1][nIter-1] + yPos/(np.sqrt(xPos**2+yPos**2+zPos**2))
    nuevazPos = lista_Pos[2][nIter-1] + zPos/(np.sqrt(xPos**2+yPos**2+zPos**2))

    lista_Pos[0].append(nuevaxPos)
    lista_Pos[1].append(nuevayPos)
    lista_Pos[2].append(nuevazPos)

    return lista_Pos


nPasos3D = 1000

camino3D=[[0.],[0.],[0.]]
for d in range(1,nPasos3D):
    camino3D=CaminoAleatorio3D(camino3D,d)
  
ax=plt.axes(projection="3d")
ax.plot3D(camino[0],camino[1],camino3D[2] ,c="m", lw=0.5)
ax.set_title("Caminos aleatorios 3D")
plt.show()

