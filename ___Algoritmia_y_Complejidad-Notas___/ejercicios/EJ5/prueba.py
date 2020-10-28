class trabajo_object:
    def __init__(self, trabajo, plazo, ganancia):
        self.trabajo = trabajo
        self.plazo = plazo
        self.ganancia = ganancia


print("1 ------------------")
arr1 = []
listas1 = {"T1":[5,200],"T2":[3,180],"T3":[3,190],"T4":[2,300],"T5":[4,120],"T6":[2,100]}
for key, value in listas1.items():
    object1 = trabajo_object(key,value[0],value[1])
    arr1.append(object1)

sorted_arr1 = sorted(arr1, key=lambda x: x.ganancia, reverse=True)

print("Tabla en orden de ganancia")
for key in sorted_arr1:
    print(key.trabajo, key.plazo, key.ganancia)

iterations = max(key.plazo for key in sorted_arr1)

result = [0] * iterations

trabajos = ['-1'] * iterations

for i in range(len(sorted_arr1)):

    for j in range(min(iterations - 1, sorted_arr1[i].plazo - 1), -1, -1):

        if result[j] == 0:
            result[j] = 1
            trabajos[j] = sorted_arr1[i]
            break

i = 0
print(trabajos)
while i < len(trabajos)-1:
    if trabajos[i].plazo > trabajos[i+1].plazo:
        if trabajos[i+1].plazo >= i:
            temp = trabajos[i]
            trabajos[i] = trabajos[i+1]
            trabajos[i+1] = temp
    elif trabajos[i].plazo == trabajos[i+1].plazo:
        if trabajos[i].ganancia < trabajos[i+1].ganancia:
            temp = trabajos[i]
            trabajos[i] = trabajos[i+1]
            trabajos[i+1] = temp
    i+=1

tsum = 0
print ("\nOrden de Seleccion")
for item in trabajos:
    print(item.trabajo)
    tsum += item.ganancia

print("a.) Sí se completan todos los trabajos en el cronograma óptimo")
print("b.) La ganancia máxima obtenida es", tsum)
print("c.) La complejidad del algoritmo sería n^2")
