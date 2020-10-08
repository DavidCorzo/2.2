import numpy as np
import sympy as sp
from scipy.linalg import null_space

A_1 = sp.Matrix([
    [1, 0, -1],
    [1, 1, 1]
])

A_2 = sp.Matrix([
    [1, 1, -1],
    [1, 5, 1],
    [1, -1, -2]
])

A_3 = sp.Matrix([
    [1, 1, 0, 1],
    [0, 1, -1, 1],
    [0, 1, -1, -1]
])

A_4 = sp.Matrix([
    [2, -4, 0, 2, 1],
    [-1, 2, 1, 2, 3],
    [1, -2, 1, 4, 4]
])

print("1"+"-"*30)
print("Matriz :", A_1)
#Encontrar el rango
RangoA_1= np.linalg.matrix_rank(np.array(A_1).astype(np.float64))
print(f"Rango de A_1: {RangoA_1}")
#Encontrar la nulidad
num_rows, num_cols = np.array(A_1).astype(np.float64).shape
nulidadA_1 = num_cols - RangoA_1
print(f"La nulidad de A es: {nulidadA_1}")
#Encontrar el espacio Nulo
EspacioNuloA_1 = A_1.nullspace()
print(f"El espacio nulo de A es: \n {EspacioNuloA_1}\n")

print("2"+"-"*30)
print("Matrix: ", A_2)
#Encontrar el rango
RangoA_2 = np.linalg.matrix_rank(np.array(A_2).astype(np.float64))
print(f"Rango A_2: {RangoA_2}")
#Encontrar la nulidad
num_rows, num_cols = np.array(A_2).astype(np.float64).shape
nulidadA_2 = num_cols - RangoA_2
print(f"Nulidad A_2: {nulidadA_2}")
#Encontrar el espacio Nulo
EspacioNuloA_2 = A_2.nullspace()
print(f"Espacio nulo A_2 es: \n {EspacioNuloA_2}\n")


print("3"+"-"*30)
print("Matrix :", A_3)
#Encontrar el rango
RangoA_3 = np.linalg.matrix_rank(np.array(A_3).astype(np.float64))
print(f"Rango A_3: {RangoA_3}")
#Encontrar la nulidad
num_rows, num_cols = np.array(A_3).astype(np.float64).shape
nulidadA_3 = num_cols - RangoA_3
print(f"La nulidad de A3 es: {nulidadA_3}")
#Encontrar el espacio Nulo
EspacioNuloA_3 = A_3.nullspace()
print(f"Espacio nulo A3: \n {EspacioNuloA_3}")


print("4"+"-"*30)
print("Matrix :", A_4)
#Encontrar el rango
RangoA_4= np.linalg.matrix_rank(np.array(A_4).astype(np.float64))
print(f"Rango de A4 es: {RangoA_4}")
#Encontrar la nulidad
num_rows, num_cols = np.array(A_4).astype(np.float64).shape
nulidadA_4 = num_cols - RangoA_4
print(f"La nulidad de A4 es: {nulidadA_4}")
#Encontrar el espacio Nulo
EspacioNuloA_4 = A_4.nullspace()
print(f"Espacio nulo de A_4 es: \n {EspacioNuloA_4}")
