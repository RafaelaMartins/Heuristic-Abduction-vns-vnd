from enum import Enum 

class State(Enum):

    UNVISITED = 0,
    VISITED = 1, 
    COLORFUL = 2
    
class Vertex():

    def __init__(self, label):
        self.label = label
        self.color = None
        self.degree = 0
        self.state = State.UNVISITED

    def change_state(self, state: State):
        self.state = state

    def set_color(self, color):
        self.color = color


class Graph():

    def __init__(self, file_name):
        self.num_vertex = 0
        self.num_edges = 0
        self.edges = {}
        self.vertices = []
        self.optimal_color = 0
        self.read_graph(file_name)

    def add_edge(self, v, w):
        if v not in self.edges:
            self.edges[v] = [w]
        else:
            self.edges[v].append(w)

        if w not in self.edges:
            self.edges[w] = [v]
        else:
            self.edges[w].append(v)

    def vertex_list(self):
        #return [v for v in self.edges]
        return self.vertices[1:]

    def calc_degree(self, v: Vertex):
        list = self.edges[v.label]
        v.degree = len(self.edges[v.label])

    def adjacent_list(self, v: Vertex):
        return [self.vertices[int(label)] for label in self.edges[v.label]]

    def __str__(self):
        res = "vertices: "
        for k in self.edges:
            res += k + " "
        res += "\nedges: "
        for k in self.edges:
            for e in self.edges[k]:
                res += "(" + k + ", " + e + "), "
            res += "\n"
        return res

    def read_graph(self, file_name):
        with open(file_name,'r') as file:
            for line in file:
                if line not in ('','\n'):
                    args = line.split()
                    if args[0] == 'e':
                        self.add_edge(args[1], args[2])
                    elif args[0] == 'o':
                        self.optimal_color = int(args[1])
                    elif args[0] == 'p':
                        self.num_vertex = int(args[2])
                        self.num_edges = int(args[3])
                        self.create_vertices()

    def create_vertices(self):
        self.vertices = [None]
        for i in range(1,self.num_vertex+1):
            v = Vertex(str(i))
            self.vertices.append(v)
            self.edges[v.label] = []

    # Calcula o número de cores do grafo passado por parâmetro
    def calculate_number_colors(self):
        
        # Lista com as cores encontradas no grafo
        colors = []

        # Percorrendo todos os vértices do grafo
        for i in range(1, self.num_vertex + 1):

            # Se a cor de um determinado vértice não estiver na lista de cores
            if self.vertices[i].color not in colors:
                # A cor é colocada na lista de cores
                colors.append(self.vertices[i].color)

        # Ao final é retornado o número de cores encontrado
        return len(colors)