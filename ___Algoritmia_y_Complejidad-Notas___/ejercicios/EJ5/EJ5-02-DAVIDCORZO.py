class trabajos:
    def __init__(self, name:str, datos:int):
        self.name = name
        self.datos = datos

        
if __name__ == "__main__":
    arr = list()
    for name,datos in zip(
        ["a","b","c","d","e","f"],
        [40,10,20,15,25,30]):
        l = trabajos(name, datos)
        arr.append(l)
    
    sorted_arr = sorted([x.datos for x in arr])
    print(sorted_arr)
    a = []
    s = sorted_arr[0] + sorted_arr[1]
    for i in sorted_arr[2:]:
        a.append(s)
        s += i
    a.append(s)

    print(sum(a))
