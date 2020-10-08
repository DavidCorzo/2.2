library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Data.xlsx",sheet="Mcuadratico")

#ingresar arrays a funcion polyfit
p <- polyfit(datos$Level, datos$Salary, 2)

#mostrar coeficientes
p

#graficar data
plot(datos$Level, datos$Salary, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Parabola de mejor ajuste")

#graficar recta de ajuste
yf <- polyval(p, datos$Level)
lines(datos$Level, yf, col="blue")

