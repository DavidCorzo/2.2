library('pracma')

# 1. 
print("1.\n")
A <- matrix(data=sample.int(10,1500,TRUE), nrow=15, ncol=15)
print("Matriz A: ")
print(A)
B <- matrix(data = sample.int(10, 1500, TRUE), nrow = 15, ncol = 15)
print("Matriz B:")
print(B)

# 2.
print("2.\n")
print("Suma A+B")
print(A+B)
print("\n")

# 3.
print("3.\n")
print("Resta A-B")
print(A-B)
print("\n")

# 4.
print("4.\n")
print("Producto elemento a elemento A*B")
print(A*B)
print("\n")

# 5.
print("5.\n")
print("Producto matricial BA")
print(B%*%A)
print("\n")

# 6.
print("6.\n")
print("Forma escalonada reducida de la matriz A:")
print(rref(A))
print("\n")

# 7. 
print("7.\n")
print("Forma escalonada reducida de la matriz B:")
print(rref(B))
print("\n")
