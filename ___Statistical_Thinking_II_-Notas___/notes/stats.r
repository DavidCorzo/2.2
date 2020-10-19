library(readr)

ruta <- file.choose()

dataw <- read.csv(ruta, sep=";")

wilcox.test(
    dataw$Aditivo.1,
    dataw$Aditivo.2,
    alternative="two.sided",
    mu = 0
)


