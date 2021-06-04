from heapq import heappop, heappush
from graph import Graph

class Grasp():

    def __init__(self, alfa, iter):

        self.Graph = Graph('data/queen5_5.col')
        self.ordered_vertices = []
        self.temp = []
        self.color = 1
        self.alfa =  alfa
        self.iter = iter
        self.idx = 0
        self.solution = [None]*self.Graph.num_vertex()
        self.best_solution = [None]*self.Graph.num_vertex()
        self.run()

    def run(self):
        self.initialize()
        self.solve()
        for v in self.Graph.vertex_list():
            print(v.color)

    def initialize(self):
    
        # priority queue
        
        for v in self.Graph.vertex_list():
            self.Graph.calc_degree(v)
            entry = (v.degree, self.count, v)
            heappush(self.ordered_vertices, entry)

    def solve(self):

        for _ in range(self.iter):
            self.construction()
            #self.local_search()

    def construction(self):
        rcl = []
        sol = []
        for _ in range(self.Graph.num_vertex):
            rcl = self.create_rcl(rcl, sol)
            if rcl == []:
                self.color += 1
                sol = []
                break
            v = rcl[randint(0, len(rcl)-1)]
            v.set_color(self.color)
            solution[int(v.label)]
            sol.append(v)
            rcl.remove(v)

    def create_rcl(self, rcl, sol):
        for v in rcl:
            entry = (v.degree, self.count, v)
            heappush(self.ordered_vertices, entry)
            rcl.remove(v)
        while len(rcl) <= self.Graph.num_vertex*self.alfa:
            neighborhood = False
            _,_,v = heappop(self.ordered_vertices)
            for w in self.Graph.adjacent_list(v):
                if w in sol:
                    self.temp.append(v)
                    neighborhood = True
                    break
            if not neighborhood:
                rcl.append(v)
        return rcl

    @property
    def count():
        self.idx += 1
        return idx

Grasp(0.1, 1)