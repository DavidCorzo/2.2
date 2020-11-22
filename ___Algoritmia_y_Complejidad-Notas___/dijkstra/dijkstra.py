class Grafo:
    def __init__(self, grafo, nodo_origen='1'):
        self.grafo = grafo 
        self.nodo_origen = nodo_origen 
        self.pesos = dict() 
        self.camino = dict()
        self.nodos_restantes = list()
    
    def dijsktra(self, nodo_destino): 
        """ Encontrar matriz de adyacencia de Dijsktra. """
        for node in self.grafo: # n
            self.pesos[node] = float("inf")
            self.camino[node] = None
            self.nodos_restantes.append(node)
            
        self.pesos[self.nodo_origen] = 0 
        while len(self.nodos_restantes) != 0: 
            llave_minima = min(self.nodos_restantes) 
            nodo_actual = llave_minima 
            self.nodos_restantes.remove(nodo_actual) 
            
            for nodo in self.grafo[nodo_actual]: 
                nuevo_peso = self.grafo[nodo_actual][nodo] + self.pesos[nodo_actual]
                if self.pesos[nodo] > nuevo_peso:
                    self.pesos[nodo] = nuevo_peso
                    self.camino[nodo] = nodo_actual

        print(f'The path between {self.nodo_origen} to {nodo_destino}')
        order = list()
        order.append(nodo_destino)
        while True:
            nodo_destino = self.camino[nodo_destino]
            if nodo_destino is None:
                break
            order.insert(0,nodo_destino)
        print("->".join(order))
        
if __name__ == "__main__":
    grafo = {
        '1': {'2':2, '3':4}, 
        '2': {'3':1, '4':7}, 
        '3': {'5':3}, 
        '4': {'6':1}, 
        '5': {'4':2, '6':5}, 
        '6': {}
    }
    g = Grafo(grafo, '1')
    g.dijsktra('6')
