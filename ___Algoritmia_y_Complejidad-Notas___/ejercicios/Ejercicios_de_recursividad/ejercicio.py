import pdb, time

def b_n(b: int,n: int):
    # Función recursiva que calcule b^n si b > 0, n >= 0 pertenece a los números enteros.
    if (n == 0):
        return 1
    else: 
        return b * b_n(b, n-1)

def conejos_fib(n):
    # Alguien compra una pareja de conejos. Luego de un mes esos conejos son adultos Después de dos meses esa pareja de conejos da a luz a otra pareja de conejos. Al tercer mes la primera pareja de conejos da a luz a otra pareja de conejos y sus primeros hijos se vuelven adultos. Caca mes que pasa, cada pareja de conejos adutos da a luz a una nueva pareja de conejos y una pareja de conejos tarda un mes en crecer. Escriba una función recursiva que regrese cuántos conjeos adultos se tienen pasados n meses.
    if n == 0:
        return 0    
    elif n == 1:
        return 1
    else:
        return conejos_fib(n-2) + conejos_fib(n-1)

        
def main():
    start = time.perf_counter()
    b_n(56,9)
    print("{:.50f}".format(time.perf_counter() - start))
    start = time.perf_counter()
    b_n(2,100)
    print("{:.50f}".format(time.perf_counter() - start)*1000)

if __name__ == "__main__":
    main()

