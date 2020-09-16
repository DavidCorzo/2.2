import numpy as np
from scipy.optimize import linprog

print("1."+"-"*30)
C = np.array([-15.0, -10.0])                  #Coeficientes de la funcion costo a optimizar
A = np.array([
    [1/3,1/2],
    [1/3,1/6]
])    #Coeficientes de la matriz de desigualdades
B = np.array([100,80]) # Coeficientes libres

res = linprog(C, A, B, method="interior-point")
print("Respuesta", res) # Mostramos la solucion completa de la funcion
print("Zmax es: ", res.fun*-1, " En X1:", res.x[0], " y X2:", res.x[1])  # mostramos la maximizacion y sus puntos

del A,C,B

print("2."+"-"*30)
C = np.array([float(80), float(60)])                  #Coeficientes de la funcion costo a optimizar
A = np.array([[20,32]])    #Coeficientes de la matriz de desigualdades
B = np.array([25]) # Coeficientes libres
A_1 = np.array([[1,1]])
B_2 = np.array([1])

res = linprog(C, A, B, A_eq=A_1, b_eq=B_2, method="interior-point")
print("Respuesta", res)                      #Mostramos la solucion completa de la funcion
print("Zmax es: ", res.fun*-1, " En X1:", res.x[0], " y X2:", res.x[1])  # mostramos la maximizacion y sus puntos

del C,A,B,A_1,B_2
