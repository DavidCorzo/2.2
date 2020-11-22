import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def multiplicar(A,B):
    AB = [[0 for k in range(len(B[0]))] for j in range(len(A))]
    for i, row in enumerate(A):
        for j, col in enumerate([list(c) for c in zip(*B)]):
            AB[i][j] = sum([a*b for a, b in zip(row, col)])
    return AB

#devuelve vectores especificos
def column(matrix, i):
    return [row[i] for row in matrix]

def Markov(A,k):
    print("\t1)")
    #Encontrar eigenvalores y eigenvectores
    eigenvalores, eigenvectores = np.linalg.eig(A)

    #Diagonalizacion
    Q=eigenvectores
    if(A.shape[1]==2):
        #print("2x2")
        D = np.array([[eigenvalores[0], 0],
                      [0, eigenvalores[1]]])
    if (A.shape[1] == 3):
        #print("3x3")
        D = np.array([[eigenvalores[0], 0, 0],
                      [0, eigenvalores[1], 0],
                      [0, 0, eigenvalores[2]]])
    if (A.shape[1] == 4):
        #print("4x4")
        D = np.array([[eigenvalores[0], 0, 0, 0],
                      [0, eigenvalores[1], 0, 0],
                      [0, 0, eigenvalores[2], 0],
                      [0, 0, 0, eigenvalores[3]]])
    Qinv=np.linalg.inv(Q)

    print("Q = \n" + str(Q))
    print("D = \n" + str(D))
    print("Qinv = \n" + str(Qinv))
    #Encobntrar P^k
    Dn = np.linalg.matrix_power(D, k)

    Resultado = multiplicar(multiplicar(Q,Dn),Qinv)
    columna = column(Resultado, 0)
    print(f"\t3) iteraciones para alcanzar vector estacionario -> k = {k}")
    for x in Resultado:
        print(x)


    if(A.shape[1]==2):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
    if (A.shape[1] == 3):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
        plt.plot(k, columna[2], 'go')
    if (A.shape[1] == 4):
        plt.plot(k, columna[0], 'ro')
        plt.plot(k, columna[1], 'bo')
        plt.plot(k, columna[2], 'go')
        plt.plot(k, columna[3], 'yo')

############################################################################

def do(P, k):
    print("\t2) guardar y graficar los datos.")
    
    for x in range(1, k):
        Markov(P, x)

    plt.axis([0, k, -1, 5])
    plt.savefig("grafica.png")
    plt.savefig("grafica.png")
    plt.show()



#cantidad de iteraciones
k=20

#Matriz de transicion

print(f"{'-'*30}P_1{'-'*30}")
P_1 = np.array( [[0.3, 0.5], 
                [0.7, 0.5]])
do(P_1, k)

print(f"{'-'*30}P_2{'-'*30}")
P_2 = np.array([[0.7, 0.1, 0.2], 
                [0.2, 0.8, 0.1], 
                [0.1, 0.1, 0.7]])
do(P_2, k)


print(f"{'-'*30}P_2{'-'*30}")
P_3 = np.array([[0.2, 0.1, 0.4], 
                [0.1, 0.5, 0.2], 
                [0.7, 0.4, 0.4]])
do(P_3, k)


