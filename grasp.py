from heapq import heappop, heappush
from graph import Graph
from random import randint, seed
from time import time
from math import inf

ITER = 100
ALFA = 0.7

#file_name = 'data/myciel3.col'
#file_name = 'data/fpsol2.i.1.col'
#file_name = 'data/fpsol2.i.2.col'
#file_name = 'data/fpsol2.i.3.col'
#file_name = 'data/inithx.i.1.col'
#file_name = 'data/inithx.i.2.col'
#file_name = 'data/inithx.i.3.col'
#file_name = 'data/le450_5a.col'
#file_name = 'data/le450_15b.col'
#file_name = 'data/le450_25d.col'
#file_name = 'data/miles250.col'
#file_name = 'data/miles1500.col'
#file_name = 'data/mulsol.i.1.col'
#file_name = 'data/myciel3.col'
#file_name = 'data/queen5_5.col'
file_name = 'data/qg.order60.col'


optimal_color = 0
num_vertex = 0
num_edges = 0
edges = {}
degrees = []
solution = []
best_solution = []
ordered_vertices = []
count = (x for x in range(1000000000000000000)) 
result = []

# LÊ GRAFO
with open(file_name,'r') as file:
    for line in file:
        if line not in ('','\n'):
            args = line.split()
            if args[0] == 'e':
                v = args[1]
                w = args[2]
                if v not in edges:
                    edges[v] = [w]
                else:
                    edges[v].append(w)
                if w not in edges:
                    edges[w] = [v]
                else:
                    edges[w].append(v)
            elif args[0] == 'o':
                optimal_color = int(args[1])
            elif args[0] == 'p':
                num_vertex = int(args[2])
                num_edges = int(args[3])

# CALCULA GRAU DE CADA VERTICE
degrees = [None]*num_vertex
for v in edges:
    degrees[int(v)-1] = len(edges[v])

# CONSTRÓI FILA DE PRIORIDADE (ORDENAÇÃO)
def create_priority_queue():
    for v in range(num_vertex):
        if degrees[v] != None:
            entry = (degrees[v], next(count), str(v+1))
            heappush(ordered_vertices, entry)

# FASE DE CONSTRUÇÃO
def construction():
    create_priority_queue()
    solution = [0]*num_vertex
    temp = []
    colored_vertices = 0
    rcl = []
    sol = []
    color = 1
    while colored_vertices < num_vertex:
        # CRIA RCL
        for v in rcl:
            entry = (degrees[int(v)-1], next(count), v)
            heappush(ordered_vertices, entry)
        rcl = []

        while (len(rcl) <= num_vertex*ALFA) and (len(ordered_vertices) > 0):
            neighborhood = False
            _,_,v = heappop(ordered_vertices)
            if len(sol) > 0:
                for w in edges[v]:
                    if w in sol:
                        temp.append(v)
                        neighborhood = True
                        break
            if not neighborhood:
                rcl.append(v)
        if rcl == []:
            color += 1
            sol = []
            if len(temp) == 0:
                break
            for v in temp:
                entry = (degrees[int(v)-1], next(count), v)
                heappush(ordered_vertices, entry)
            temp = []
        else:
            seed(time())
            v = rcl[randint(0, len(rcl)-1)]
            solution[int(v)-1] = color
            colored_vertices += 1
            sol.append(v)
            rcl.remove(v)
    return solution


def verify_infactibility(solution):
    infactibility = False
    for v in edges:
        for adj in edges[v]:
            if solution[int(v)-1] == solution[int(adj)-1]:
                infactibility = True 
                break
    print("Infactibility: {}".format(infactibility))

# BUSCA LOCAL
def local_search(solution):
    color = max(solution)
    for v in edges:
        if solution[int(v)-1] == color:
            for c in range(color-1, 1, -1):
                infactibility = False
                for adj in edges[v]:
                    if solution[int(adj)-1] == c:
                        infactibility = True
                if not infactibility:
                    solution[int(v)-1] = c
    return solution

# ATUALIZA SOLUÇÃO
def update_solution(solution, best_solution):
    if best_solution == []:
        return solution
    if max(solution) < max(best_solution):
        return solution
    else:
        return best_solution

# GRASP
for _ in range(ITER):
    start = time()
    solution = construction()
    solution = local_search(solution)
    total_time = time() - start
    result.append([total_time, max(solution)])
    best_solution = update_solution(solution, best_solution)
    

# verify_infactibility(best_solution)

# Calcula densidade do grafo
density = (num_edges/(num_vertex*(num_vertex-1)))*100

# cria conteúdo 
content = 'file = {}\nOptimal Color = {}\nDensity = '.format(file_name, optimal_color)+\
        '{0:.2f} %'.format(density)+'\n\n'
content += 'Best Solution: {}\n\n'.format(max(best_solution))
content += 'ITER,FIND_COLOR,TIME\n\n'    # MIN\tMAX\tMÉDIA\tMEDIANA\tVARIÂNCIA\tDESVIO\tQ1\tQ3\n\n

for i in range(1,ITER):
    content += '{},{},'.format(i, result[i][1]) + \
               '{0:.4f}\n'.format(result[i][0])

with open('data/grasp/'+file_name.split('/')[1]+"_result", "w") as file:
    file.write(content)
