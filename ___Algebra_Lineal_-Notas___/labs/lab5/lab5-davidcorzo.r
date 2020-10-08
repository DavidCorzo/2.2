
A <- matrix(c(1,1,0, 1,0,1, 0,1,0),3,3)

b1 <- matrix(c(1,2,4),3,1)

B <- matrix(c(1,1,0,1, 1,0,1,0, 0,1,0,0, 0,1,0,0),4,4)
b2 <- matrix(c(1,8,4,5),4,1)

print("1.\n")
det_A <- det(A)
det_A
I = diag(1,nrow=3)
det_A2 <- det(B)
det_A2

I2 = diag(1,nrow=4)
print("2.\n")
if (det_A != 0) {
  inv_A <- solve(A,I)
  inv_A
} else {
  print("No invertible.\n")
}
if (det_A != 0) {
  res <- solve(t(A)%*%A)%*%t(A)%*%b1
  res
}
if (det_A2 != 0) {
  inv_B <- solve(B,I2)
  inv_B
} else {
  print("No se puede sacar inversa")
}
if (det_A2 != 0) {
  r2 <- solve(t(B)%*%B)%*%t(B)%*%b2
  r2
}
