print("1:",quote=FALSE)
num_1 = 10 
num_2 = 2
print(sprintf("num_1: %i, num_2: %i",num_1,num_2),quote=FALSE)

print("2: vector resultados ",quote=FALSE)
A = c()
A <- c(A, num_1 + num_2)
A <- c(A, num_1 - num_2)
A <- c(A, num_1 * num_2)
A <- c(A, num_1 / num_2)
A <- c(A, num_1 ** num_2)
print(A)

print("3:",quote=FALSE)
print(sprintf("Suma num_1 (%i) y num_2 (%i): %i",num_1,num_2,A[1]),quote=FALSE)
# print(sprintf("Resta num_1 (%i) y num_2 (%i): %i",num_1,num_2,A[2]),quote=FALSE)
# print(sprintf("Multiplicación num_1 (%i) y num_2 (%i): %i",num_1,num_2,A[3]),quote=FALSE)
# print(sprintf("División num_1 (%i) y num_2 (%i): %i",num_1,num_2,A[4]),quote=FALSE)

print("4:",quote=FALSE)
B = rbind(c(1,2,3,4,5,6,7), c(1,2,3,4,5,6,7), c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7))
print(B)

print("5.",quote=FALSE)
for (row in 1:nrow(B)) {
    B[row,row] = B[row,row] + 2
}
print(B)
