# Script gerador do modelo AMPL para resolução do problema
# de coloração de vértices.

from graph import Graph
from math import inf
from itertools import count

# cria grafo
# file_name = 'myciel3.col'
# file_name = 'queen5_5.col'
file_name = 'miles250.col'
#file_name = 'inithx.i.1.col'
#file_name = 'le450_5a.col'
graph = Graph(file_name)

my_count = count(1,1)

with open(file_name+'.dat', 'w') as file:
    
    content = ''.join(
        ['var c'+str(i+1)+' binary;\n' for i in range(graph.num_vertex)])
    
    content += ''.join(
        ['var v'+str(v+1)+'c'+str(c+1)+' binary;\n' 
         for c in range(graph.num_vertex) for v in range(graph.num_vertex)])
    
    content += '\nminimize numCores : '+\
        ''.join(['c'+str(i+1)+' + ' for i in range(graph.num_vertex)])[:-3]
    
    content += ';\n\nsubject to\n\n'+\
        ''.join(['r'+str(next(my_count))+': '+\
        ''.join(['v'+str(v+1)+'c'+str(i+1)+' + ' for i in range(graph.num_vertex)])[:-3] +\
        ' = 1;\n' for v in range(graph.num_vertex)])

    content += ''.join(
        ['r'+str(next(my_count))+': v'+v.label+'c'+str(i+1)+
        ' + '+'v'+w+'c'+str(i+1)+' <= c'+str(i+1)+';\n'
        for v in graph.vertex_list() for w in graph.edges[v.label] 
        for i in range(graph.num_vertex)])
    
    content += '\nsolve;\ndisplay numCores;'
    file.write(content)