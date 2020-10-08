require(Matrix)
require(pracma)

# Funcion para generar el espacio nulo
EspacioNulo <- function (A) {
    m <- dim(A)[1]; n <- dim(A)[2]
    QR <- base::qr.default(A)
    r <- QR$rank
    if ((r < min(m, n)) || (m < n)) {
		R <- QR$qr[1:r, , drop = FALSE]
		P <- QR$pivot
		F <- R[, (r + 1):n, drop = FALSE]
		I <- base::diag(1, n - r)
		B <- -1.0 * base::backsolve(R, F, r)
		Y <- base::rbind(B, I)
		X <- Y[base::order(P), , drop = FALSE]
		return(X)
    }
    return(base::matrix(0, n, 1))
}

A_1 <- matrix(
	c(1,1, 0,1, -1,1)
	,2 ,3)

A_2 <- matrix(
	c(1, 1, 1, 1, 5, -1, -1, 1,-2)
	,3, 3)

A_3 <- matrix(
	c(1, 0, 0, 1, 1, 1, 0, -1, -1, 1, 1, -1)
	,3, 4 )
A_4 <- matrix(c(2,-1,1, -4,2,-2, 0,1,1, 2,2,4, 1,3,4)
	,3,5)

print("1. ")
print(A_1)

# Encontrar el rango
RangoA_1 <- rankMatrix(A_1)[1]
# Encontrar la nulidad
nulidadA_1 <- ncol(A_1) - RangoA_1
# Encontrar el espacio nulo
EspacioNuloA_1 <- EspacioNulo(A_1)

RangoA_1
nulidadA_1
EspacioNuloA_1

print("2. ")
print(A_2)

# Encontrar el rango
RangoA_2 <- rankMatrix(A_2)[1]
# Encontrar la nulidad
nulidadA_2 <- ncol(A_2) - RangoA_2
# Encontrar el espacio nulo
EspacioNuloA_2 <- EspacioNulo(A_2)

RangoA_2
nulidadA_2
EspacioNuloA_2

print("3. ")
print(A_3)

# Encontrar el rango
RangoA_3 <- rankMatrix(A_3)[1]
# Encontrar la nulidad
nulidadA_3 <- ncol(A_3) - RangoA_3
# Encontrar el espacio nulo
EspacioNuloA_3 <- EspacioNulo(A_3)

RangoA_3
nulidadA_3
EspacioNuloA_3

print("4 --------------")
print(A_4)

# Encontrar el rango
RangoA_4 <- rankMatrix(A_4)[1]
# Encontrar la nulidad
nulidadA_4 <- ncol(A_4) - RangoA_4
# Encontrar el espacio nulo
EspacioNuloA_4 <- EspacioNulo(A_4)

RangoA_4
nulidadA_4
EspacioNuloA_4
