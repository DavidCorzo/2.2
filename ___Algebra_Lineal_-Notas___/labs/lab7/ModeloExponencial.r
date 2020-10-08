library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Data.xlsx",sheet="Mexponencial")
datos$Dia = datos$Dia - datos$Dia[1]
#ingresar arrays a funcion polyfit
p <- polyfit(datos$Dia, log(datos$Casos), 1)

#mostrar coeficientes
r <- p[1]
Po <- exp(p[2])
r
Po

#graficar data
plot(datos$Dia, datos$Casos, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Modelo exponencial")

#graficar Modelo Exponencial
yf <- Po * exp(r*datos$Dia)
lines(datos$Dia, yf, col="blue")
