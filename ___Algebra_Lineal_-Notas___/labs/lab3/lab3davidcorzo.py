import numpy as np
import sympy as sp 

# 1. CREACION DE MATRIZ A Y B
print("-"*10+"1"+"-"*10)
A = np.random.randint(low=-10,high=10,size=(15,15))
print(f"Matriz A: \n{str(A)}")
B = np.random.randint(low=-10,high=10,size=(15,15))
print(f"Matriz B: \n{str(B)}")

# 2. SUMA
print("-"*10+"2"+"-"*10)
print(f"Suma A + B \n{str(A+B)}")

# 3. DIFERENCIA DE MATRICES
print("-"*10+"3"+"-"*10)
print(f"Resta A - B \n{str(A-B)}")

# 4. PUNTO ELEMENTO A ELEMENTO
print("-"*10+"4"+"-"*10)
print(f"Producto elemento a elemento A * B \n{str(A * B)}")

# 5. Producto matricial
print("-"*10+"5"+"-"*10)
print(f"Producto matricial BA \n{str(B * A)}")

# 6. FERR
print("-"*10+"6"+"-"*10)
A = sp.Matrix(A)
print(f"Forma escalondada reducida de matriz A: \n{str(A.rref())}")

# 7. FERR
print("-"*10+"7"+"-"*10)
B = sp.Matrix(B)
print(f"Forma escalondada reducida de matriz B: \n{str(B.rref())}")

