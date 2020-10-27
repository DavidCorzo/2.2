class trabajos:
    def __init__(self, name:str, plazos:int, ganancias:int):
        self.name = name
        self.plazos = plazos 
        self.ganancias = ganancias

        
if __name__ == "__main__":
    arr = list()
    for name,plazos,ganancias in zip(
        ["T1","T2","T3","T4","T5","T6"],
        [5, 3, 3, 2, 4, 2],
        [200, 180, 190, 300, 120, 100]):
        l = trabajos(name, plazos, ganancias)        
        arr.append(l)
    
    print(sorted([x.ganancias for x in arr]))
    

    
    
    print(max([x.ganancias for x in arr]))
