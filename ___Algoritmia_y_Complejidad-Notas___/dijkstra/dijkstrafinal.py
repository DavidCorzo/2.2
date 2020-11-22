import networkx as nx
import matplotlib.pyplot as plt
import os

def make_new_name(filename:str):
    i = 0
    while os.path.exists(f'{filename}{i}.png'):
        i += 1
    return f'{filename}{i}.png'

class Grafo:
    def __init__(self, grafo, nodo_origen='1'):
        self.grafo = grafo 
        self.nodo_origen = nodo_origen 
        self.pesos = dict() 
        self.camino = dict()
        self.nodos_restantes = list()

    def dibujar_grafica(self, forma="circular"):
        graph = nx.Graph()
        for nodo in grafo:
            grafo[nodo]
            for nodo2 in grafo[nodo]:
                print(f"{nodo} : {nodo2}")
                graph.add_edge(nodo, nodo2, weight=grafo[nodo][nodo2])
        if forma == "circular":
            pos = nx.circular_layout(graph)
        else:
            pos = nx.planar_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos,edge_labels=labels)
        plt.savefig(make_new_name("grafo"))

    
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
    g.dibujar_grafica("plano")
