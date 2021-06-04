from vnd import VND
from graph import Graph
import time
import numpy

ITER = 101

#file_name = 'myciel3.col'
#file_name = 'fpsol2.i.1.col'
#file_name = 'fpsol2.i.2.col'
#file_name = 'fpsol2.i.3.col'
#file_name = 'inithx.i.1.col'
#file_name = 'inithx.i.2.col'
#file_name = 'inithx.i.3.col'
#file_name = 'le450_5a.col'
#file_name = 'le450_15b.col'
#file_name = 'le450_25d.col'
#file_name = 'miles250.col'
#file_name = 'miles1500.col'
#file_name = 'mulsol.i.1.col'
#file_name = 'myciel3.col'
#file_name = 'queen5_5.col'
file_name = 'qg.order60.col'


result = []

# Inicia a marcação do tempo
start = time.time()

# roda VND ITER vezes e salva resultados
path = 'data/'+file_name
graph = Graph(path)
optimal_color = graph.optimal_color
density = (graph.num_edges/(graph.num_vertex*(graph.num_vertex-1)))*100

for i in range(ITER):
	print(i)
	result.append(VND(path))


# cria conteúdo 
content = 'file = {}\nOptimal Color = {}\nDensity = '.format(file_name, optimal_color)+\
        '{0:.2f} %'.format(density)+'\n\n'

content += 'ITER,FIND_COLOR,TIME\n\n'    # MIN\tMAX\tMÉDIA\tMEDIANA\tVARIÂNCIA\tDESVIO\tQ1\tQ3\n\n

for i in range(1,ITER):
    content += '{},{},'.format(i, result[i].color) + \
               '{0:.4f}\n'.format(result[i].total_time)
colors = []

for i in range(ITER):
	colors.append(result[i].color)

content += '\nINST: {}'.format(file_name)
content += '\nMIN COLOR: {}'.format(min(colors))
content += '\nMEAN: {}'.format(numpy.mean(colors))
content += '\nMAX COLOR: {}'.format(max(colors))
content += '\nSD: {}'.format(numpy.std(colors))
content += '\nVAR: {}'.format(numpy.var(colors))

with open('data/vnd/'+file_name+"_result", "w") as file:
    file.write(content)

# Termina a marcação do tempo
end = time.time()

# Calculando o tempo
t = end - start

print("Total time execution:",t)
