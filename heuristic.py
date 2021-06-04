# Solver Heurístico para a coloração de vértices

from graph import Graph, State
from heapq import heappop, heappush
from itertools import count
from random import randint
from plot import generate_dot
from time import time

class heuristic():

    def __init__(self, file_name):
        init_time = time()
        self.graph = Graph(file_name)

        # variáveis
        ordered_vertices = []
        temp = []
        color = 0
        my_count = count(1,1)

        # cria lista ordenada de vértices por grau (priority queue)
        list = self.graph.vertex_list()
        for v in self.graph.vertex_list():
            self.graph.calc_degree(v)
            entry = (self.graph.num_vertex - v.degree, next(my_count), v)
            heappush(ordered_vertices, entry)

        # Solver
        while len(ordered_vertices) > 0:
            color += 1
            while len(ordered_vertices) > 0:
                entry = heappop(ordered_vertices)
                v = entry[2]
                
                # aleatoriedade
                same_degree = [v]
                if len(ordered_vertices) > 0:
                    entry = heappop(ordered_vertices)
                    while entry[2].degree == v.degree:
                        same_degree.append(entry[2])
                        if len(ordered_vertices) > 0:
                            entry = heappop(ordered_vertices)
                        else:
                            break
                    if entry[2].degree != v.degree:
                        heappush(ordered_vertices, entry)
                chosen = randint(0, len(same_degree)-1)
                v = same_degree[chosen]
                for i, w in enumerate(same_degree):
                    if i != chosen:
                        entry = (self.graph.num_vertex - w.degree, next(my_count), w)
                        heappush(ordered_vertices, entry)
                same_degree = []

                if v.state == State.UNVISITED:
                    v.set_color(color)
                    for w in self.graph.adjacent_list(v):
                        w.change_state(State.VISITED)
                    v.change_state(State.COLORFUL)
                else:
                    entry = (self.graph.num_vertex - v.degree, next(my_count), v)
                    heappush(temp, entry)
            ordered_vertices = temp
            temp = []
            for _,_,v in ordered_vertices:
                v.change_state(State.UNVISITED)

        # imprime resultado
        print('Total de cores: {}'.format(color))

        # Melhora o resultado
        # for v in self.graph.vertex_list():
        #     list = [w.color for w in self.graph.adjacent_list(v)]
        #     for c in range(1, v.color):
        #         if c in list:
        #             pass
        #         else:
        #             v.color = c
        #             break

        # exclui cores não utilizadas
        # list = [v.color for v in self.graph.vertex_list()]
        # aux = color
        # for c in range(1,aux):
        #     if c not in list:
        #         color -= 1

        # imprime resultado
        # print('Total de cores: {}'.format(color))

        # verifica
        
        for v in self.graph.vertex_list():
            list = [w.color for w in self.graph.adjacent_list(v)]
            if v.color in list:
                print('TRUE')
            list = []

        self.color = color
        self.total_time = time() - init_time