library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Datos.xlsx",sheet="Lineal")

#ingresar arrays a funcion polyfit
p <- polyfit(datos$x, datos$y, 1)

#mostrar coeficientes
p

#graficar data
plot(datos$x, datos$y, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Recta de mejor ajuste")

#graficar recta de ajuste
yf <- polyval(p, x)
lines(datos$x, yf, col="blue")
