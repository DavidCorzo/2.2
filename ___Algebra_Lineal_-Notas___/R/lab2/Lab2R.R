library(ggplot2)
library(tidyverse)

f1 <- function(x) {       #f(x)=1-x
  x+6
}

f2 <- function(x) {       #f(x)=x-4
  6-x
}

f3 <- function(x) {       #f(x)=x+4
  2*x-10
}


#vector con valores de x, en este caso entre -10 y 10
x = c(0, 23)



grafica <- ggplot(data.frame(x), aes(x = x)) +   #eje x toma los valores de -10 a 10
  stat_function(fun = f1)+                      #se asignan las funciones a la grafica
  stat_function(fun = f2)+
  stat_function(fun = f3)

grafica <- ggplot(data.frame(x = c(0, 23)), aes(x = x)) +   #agregar leyendas a las graficas
  stat_function(fun = f1,aes(colour = "f1"))+                                    
  stat_function(fun = f2,aes(colour = "f2"))+
  stat_function(fun = f3,aes(colour = "f3"))+
  scale_colour_manual("Funciones",values = c("red","blue", "orange"))


grafica <- grafica + scale_x_continuous(name = "X",
                    breaks = seq(0, 23, 2)) +               #cambia el nombre de los ejes y ajusta escala de eje x
                     scale_y_continuous(name = "Y")

grafica <- grafica + ylim(0,25)


grafica <- grafica + ggtitle("Grafica de las 3 rectas")       #asigna titulo a la grfica


plot(grafica)           #imprime la grafica de las funciones

ggsave("grafica1R.png")


## Grafica de la region entre las tres rectas


##Las intersecciones entre cada recta satisfacen la ec f1-f2=0
##Uniroot encuentra las raices de la funcion f1-f2
x1 = uniroot(function(x) f1(x)-f2(x),c(0,23))$root        #coordenada x de interseccion entre f1 y f2
x2 = uniroot(function(x) f1(x)-f3(x),c(0,23))$root        #coordenada x de interseccion entre f1 y f3
x3 = uniroot(function(x) f2(x)-f3(x),c(0,23))$root        #coordenada x de interseccion entre f2 y f3

y1 = f1(x1)       #coordenada y de interseccion entre f1 y f2
y2 = f1(x2)       #coordenada y de interseccion entre f1 y f3
y3 = f2(x3)       #coordenada y de interseccion entre f2 y f3


sprintf("x1,y1: %g,%g", x1,y1)  #imprime corrdenada x,y de interseccion entre f1 y f2
sprintf("x2,y2: %g,%g", x2,y2) 
sprintf("x3,y3: %g,%g", x3,y3) 

px=c(x1,x3,x2)             #se crea una tabla con todos los puntos
py=c(y1,y3,y2)
mydata2 = data.frame(x=px,y=py)

grafica2 <- ggplot(data = mydata2, aes(x = x, y = y)) +   #se realiza la grafica de la region sombreada
  geom_polygon(color=NA) + 
  theme_classic()



plot(grafica2)          #imprime la grafica de la regi?n

ggsave("grafica2.png")




