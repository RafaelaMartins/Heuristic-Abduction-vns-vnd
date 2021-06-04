from heuristic import heuristic
from graph import Graph

ITER = 101

#file_name = 'myciel3.col'
#file_name = 'fpsol2.i.1.col'
#file_name = 'fpsol2.i.2.col'
#file_name = 'fpsol2.i.3.col'
#file_name = 'inithx.i.1.col'
file_name = 'inithx.i.2.col'
#file_name = 'inithx.i.3.col'
#file_name = 'le450_5a.col'
#file_name = 'le450_15b.col'
#file_name = 'le450_25d.col'
#file_name = 'miles250.col'
#file_name = 'miles1500.col'
#file_name = 'mulsol.i.1.col'
#file_name = 'myciel3.col'
#file_name = 'queen5_5.col'


result = []

# roda heurística ITER vezes e salva resultados
path = 'data/'+file_name
graph = Graph(path)
optimal_color = graph.optimal_color
density = (graph.num_edges/(graph.num_vertex*(graph.num_vertex-1)))*100

for _ in range(ITER):
    result.append(heuristic(path))

# cria conteúdo 
content = 'file = {}\nOptimal Color = {}\nDensity = '.format(file_name, optimal_color)+\
        '{0:.2f} %'.format(density)+'\n\n'

content += 'ITER,FIND_COLOR,TIME\n\n'    # MIN\tMAX\tMÉDIA\tMEDIANA\tVARIÂNCIA\tDESVIO\tQ1\tQ3\n\n

for i in range(1,ITER):
    content += '{},{},'.format(i, result[i].color) + \
               '{0:.4f}\n'.format(result[i].total_time)

with open('data/'+file_name+"_result", "w") as file:
    file.write(content)
