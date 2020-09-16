import numpy as np
import sympy as sp
import time as tm


def ReglaCrammer(A,b):
    sol = []
    deta = round(np.linalg.det(A), 1)

    for i in range(len(b)):
        B = A.copy()
        B[:, i] = b
        detb = round(np.linalg.det(B), 1)
        sol.append(detb / deta)
    return sol


A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])

B = np.array([
    [1,1,0,1],
    [1,0,1,0],
    [0,1,0,0],
    [0,1,0,0]
])

b1 = np.array([
    [1],
    [2],
    [4]
])

b2 = np.array([
    [1],
    [8],
    [4],
    [5]
])

print("1"+"-"*30)
# Calcule los determinantes e inversas (usando numpy y sympy) de A y B.
detA_n = np.linalg.det(A)
detB_n = np.linalg.det(B)
print(f"Numpy: Inversa de A {detA_n} & B {detB_n}")
detA_s = sp.Matrix(A).det()
detB_s = sp.Matrix(B).det()
print(f"Sympy: Inversa de A {detA_s} & B {detB_s}")

if detA_n != 0:
    invA_n = np.linalg.inv(A)
    invA_s = sp.Matrix(A).inv()
    print(f"Numpy: Inversa de A\n{invA_n}\n\nSympy: Inversa de A\n{invA_s}\n")
else: print("No invertible\n")
if detB_s != 0:
    invB_n = np.linalg.inv(B)
    invB_s = sp.Matrix(B).inv()
    print(f"Numpy: Inversa de A\n{invA_n}\n\nSympy: Inversa de B\n{invB_s}\n")
else: print("No invertible\n")


print("2"+"-"*30)
if detA_n != 0:
    start = tm.time()
    sol_A_n = np.dot(invA_n,b1)
    end = tm.time()
    print(f"Numpy time A: {end-start}")
    start = tm.time()
    sol_A_s = np.dot(invA_s,b1)
    end = tm.time()
    print(f"Sympy time A: {end-start}")
    start = tm.time()
    sol_A_r = ReglaCrammer(A,b1.transpose())
    print(f"Cramer time A: {end-start}")
else: print("No invertible.\n")
if detB_n != 0:
    start = tm.time()
    sol_B_n = np.dot(invB_n,b1)
    end = tm.time()
    print(f"Numpy time B: {end-start}")
    start = tm.time()
    sol_A_s = np.dot(invA_s,b1)
    end = tm.time()
    print(f"Sympy time B: {end-start}")
    start = tm.time()
    sol_A_r = ReglaCrammer(B,b1.transpose())
    print(f"Cramer time B: {end-start}")
else: print("No invertible.\n")


print("3"+"-"*30)
C = np.random.randint(0,5,(15,15))
c1 = np.random.randint(0,5,(15,1))

det_A = np.linalg.det(C)
print(f"Numpy: Determinante C: \n{det_A}\n")
det_A2 = sp.Matrix(C).det()
print(f"Sympy: Determinante C: \n{det_A2}\n")

if det_A2 != 0:
    inv_A = np.linalg.inv(C)
    print(f"Numpy: Inversa C con numpy: \n{inv_A}\n")
    inv_a2 = sp.Matrix(C).inv()
    print(f"Sympy: Inversa C: \n{inv_a2} \n")

    print("Inversa Numpy C")
    start = tm.time()
    n_1 = np.dot(inv_A, c1)
    end = tm.time()
    print(n_1)
    print(f"Numpy time C: {end-start}\n")

    print("Inversa Sympy C\n")
    start = tm.time()
    n_2 = np.dot(inv_a2, c1)
    end = tm.time()
    print(n_2)
    print(f"Sympy time C: {end-start}")

    print("Regla de Cramer C")
    start = tm.time()
    r_1 = ReglaCrammer(C, c1.transpose())
    end = tm.time()
    print(r_1)
    print(f"Cramer C: {end-start}")
else:
    print("\nInversa no existe \n")

print("4"+"-"*30)
C = np.random.randint(0,3,(15,15))
c1 = np.random.randint(0,3,(15,1))

det_A = np.linalg.det(C)
print(f"Determinante C con numpy: \n{det_A}\n")
det_A2 = sp.Matrix(C).det()
print(f"Determinante C con sympy: \n{det_A2}\n\n")

if det_A2 != 0:
    inv_a = np.linalg.inv(C)
    print(f"Numpy: Inversa de C: \n {inv_a}\n")
    inva2 = sp.Matrix(C).inv()
    print(f"Sympy: inversa C: \n {inva2}\n")

    print("\nInversa Numpy C\n")
    start = tm.time()
    n_1 = np.dot(inv_a, c1)
    end = tm.time()
    print(n_1)
    print(f"Numpy C: {end-start}\n")

    inicio=tm.time()
    print("\nInversa Sympy C\n")
    n_2 = np.dot(inva2, c1)
    end = tm.time()
    print(n_2)
    print(f"Sympy C: {end-start}\n")

    print("Regla de Cramer C\n")
    start = tm.time()
    r_1 = ReglaCrammer(C, c1.transpose())
    print(r_1)
    end = tm.time()
    print(f"Cramer C: {end-start}\n")
else:
    print("No invertible.")

print("5"+"-"*30)
print("De los tres métodos todos prueban ser buenos, sin embargo el más ineficiente ha sido en este ejercicio sympy. Numpy y la regla de crammer salen con tiempos muy cercanos como para poder derivar alguna conclusión fuerte.")
