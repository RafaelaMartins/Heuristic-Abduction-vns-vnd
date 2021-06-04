from graph import Graph
from math import *
from random import randint
import time

class VNS():
	def __init__(self, path):
		self.color = 0
		self.total_time = 0
		self.file_name = path
		self.Graph = self.read_graph()
		self.optimal = self.Graph.optimal_color
		self.file_name_format()
		self.run()

	# Realiza a execução do VND
	def run(self):

		# Inicia a marcação do tempo
		start = time.time()

		# Número de vezes que será rodado o VNS sem que haja melhoria
		MAX_TIMER = 15

		# Variável que controla o número de repetições de acordo com o estabelicido
		timer = 0

		# Número máximo de estruturas de vizinhança
		MAX_K = 3

		# Obtendo a solução inicial
		s = self.generate_first_solution(self.Graph)

		# Solução f(s)
		f_s = s.calculate_number_colors()

		print("First solution color number:",f_s)

		# Solução f(s')
		f_sl = None

		# Enquanto o timer não ultrapassar o valor estipulado
		while timer <= MAX_TIMER:

			# Variável que controla qual estrutura de vizinhança será usada
			k = 1

			# Enquanto não forem usadas todas as estruturas de vizinhança
			while k <= MAX_K:

				result = []

				# Estrutura de vizinhança 1
				if k == 1:

					# Roda a estrutura de vizinhança 1 e atribui a melhor coloracao encontrada
					f_sl = self.runStructure(1, s)

				# Estrutura de vizinhança 2
				elif k == 2:
					f_sl = self.runStructure(2, s)
				
				# Estrutura de vizinhança 3
				else:
					# Solução f(s')
					f_sl = self.runStructure(3, s)

				# Se houver melhoria
				if self.check_improvement(f_sl, f_s):

					# É reiniciado o timer
					timer = 0

					# A nova melhor solução é atualizada
					f_s = f_sl

					# Reinicia as estruturas de vizinhança
					k = 1

				# Senão passa para a próxima estrutura de vizinhança e acrescenta o timer
				else:
					k = k + 1
					timer = timer + 1

		# Finaliza a marcação do tempo
		end = time.time()

		self.total_time = end - start
		self.color = f_s
		print("Last solution color number:",f_s)
		print("Run time:", self.total_time)

	def file_name_format(self):
		self.file_name = ''.join(self.file_name.split('.'))

	def read_graph(self):
	    with open(self.file_name,'r') as file:
	        g = Graph(self.file_name)
	        for line in file:
	            args = line.split()
	            if args[0] == 'p':
	                g.num_vertex = int(args[2])
	            if args[0] == 'e':
	                g.add_edge(args[1], args[2])
	    return g

	# Gera uma primeira solução, cada vértice do grafo possuirá uma cor
	def generate_first_solution(self, graph):
		
		# Inicia-se o número de cores
		color = 0

		# Para cada vértice no grafo
		for i in range(1, len(graph.vertices)):
			
			# É atribuída uma cor para o vértice analisado
			graph.vertices[i].set_color(color)
			
			# Aumenta a cor a ser colocada
			color += 1

		# Retorna o grafo colorido
		return graph

	# Estrutura de vizinhança básica
	'''
		Na vizinhança básica, o movimento realizado também chamado de
		básico, consiste na mudança da classe de cor de um vértice para a melhor classe de cor
		possível
	'''
	def n_s1(self, graph):
		# Porcentagem de vértices a serem selecionados
		rate = 0.1

		# Número máximo de cores
		max_color = graph.num_vertex

		# Lista com os vértices sorteados
		sorted_vertex = []

		# Calculando o número de vértices a ser sorteado
		sort_num_vertex = ceil(graph.num_vertex * rate)

		# Lista que guarda as cores dos vértices adjacentes
		adj_colors = []

		# Sorteando os vértices
		for i in range(0, sort_num_vertex):
			sorted_vertex.append(graph.vertices[randint(1, graph.num_vertex)])

		# Escolhendo a melhor cor para os vértices selecionados
		for v in sorted_vertex:
			
			# Armazenando as cores dos adjacentes
			for adj in graph.adjacent_list(v):
				adj_colors.append(adj.color)

			# Verifica qual a melhor cor que não está nos adjacentes
			for color in range(0, max_color):
				if color not in adj_colors:
					v.set_color(color)
					break

			# Reiniciando a lista de cores adjacentes
			adj_colors = []

		# Retornando o grafo modificado
		return graph

	# Estrutura de vizinhança desenvolvida pelo grupo
	"""

	"""
	def n_s2(self, graph):
		
		# Lista com os vértices selecionados
		selected_vertices = []

		# Porcentagem que define o tamanho máximo da lista selected_vertices
		RATE = 0.1

		# Tamanho máximo da lista de vértices selecionados de acordo com a porcentagem definida
		max_len = ceil(graph.num_vertex * RATE)

		# Menor cor do grafo
		smallest_color = 0

		# Maior cor do grafo
		biggest_color = graph.num_vertex

		# Selecionando os vértices
		while len(selected_vertices) < max_len:

			# Selecionando um vértice aleatoriamente
			selected_vertex = graph.vertices[randint(1, graph.num_vertex)]

			# Se o vértice ainda não estiver na lista de vértices selecionados
			if selected_vertex not in selected_vertices:

				# Colocando o vértice na lista
				selected_vertices.append(selected_vertex)

		# Para cada vértice selecionado
		for v in selected_vertices:

			adj_colors = []

			# Armazenando as cores dos adjacentes
			for adj in graph.adjacent_list(v):
				adj_colors.append(adj.color)

			# Se o tamanho dos adjacentes for igual ao maximo de cores, então é um vértice que é totalmente ligado
			if len(adj_colors) == biggest_color:
				pass

			else:

				# Cor do vértice analisado no momento
				current_color = v.color

				# Sorteando a nova cor do vértice
				sorted_color = randint(smallest_color, biggest_color)


				while sorted_color in adj_colors:
					sorted_color = randint(smallest_color, biggest_color)

				v.set_color(sorted_color)			

		return graph

	# Estrutura de vizinhança desenvolvida pelo grupo
	"""
		Seleciona 10% dos vértices de maior cor no grafo e os colore de acordo
		com a cor do seu adjacente de maior cor, somando 1 a essa cor
	"""
	def n_s3(self, graph):
		
		# Definindo a maior cor existente no grafo
		biggest_color = self.biggest_color(graph)

		# Lista com os vértices que possuem a maior cor
		b_color_vertex = []

		# Lista com a cor dos adjacentes
		adj_colors = []

		# Porcentagem que define o tamanho máximo da lista b_color_vertex
		RATE = 0.1

		# Tamanho máximo da lista b_color_vertex
		max_len = ceil(graph.num_vertex * RATE)

		# Selecionando os vértices com a maior cor
		for i in range(1, len(graph.vertices)):
			if graph.vertices[i].color == biggest_color and len(b_color_vertex) < max_len:
				b_color_vertex.append(graph.vertices[i])

		# Percorre os vértices de maior cor
		for v in b_color_vertex:

			# Percorre os adjacentes do vértice armazenando suas cores
			for adj in graph.adjacent_list(v):
				adj_colors.append(adj.color)

			# Se a própria cor do vértice estiver na lista
			# Ou se não houverem adjacentes
			if v.color in adj_colors or not adj_colors:
				
				pass

			else:
				# Colore o vértice analisado com a maior cor dos adjacente + 1
				v.set_color(max(adj_colors) + 1)

		# Retornando o grafo
		return graph


	# Função que verifica se houve melhoria
	def check_improvement(self, s1, s2):
		
		# Se o número de cores de f(s') < f(s), então houve melhoria
		if s1 < s2:
			return True
		else:
			return False

	# Função que retorna a maior cor de um grafo
	def biggest_color(self, graph):

		# Lista das cores
		colors = []

		# Para cada vértice no grafo
		for i in range(1, len(graph.vertices)):

			# Adiciona a cor
			colors.append(graph.vertices[i].color)

		# Retorna a maior cor
		return max(colors)

	def runStructure(self, ns_number, graph):

		# Contador que controla quantas vezes o loop foi executado
		cont = 0
			
		# Coloração inicial do grafo
		initial_coloring = graph.calculate_number_colors()

		# Enquanto for verdade
		while True:
			
			# É escolhida a estrutura de vizinhança de acordo com o número passado por parâmetro
			if ns_number == 1:
				
				new_coloring = self.n_s1(graph).calculate_number_colors()
			
			elif ns_number == 2:

				new_coloring = self.n_s2(graph).calculate_number_colors()	 

			else:

				new_coloring = self.n_s3(graph).calculate_number_colors()

			# Se o contador chegar em sua contagem máxima sem melhorias'todo o processo é parado
			if cont == 10:

				break

			# Se houver alguma melhora na coloração
			if new_coloring < initial_coloring:
				
				# A melhor cor a ser batida é atualizada
				initial_coloring = new_coloring

				# E o contador reiniciado
				cont = 0
			else:

				# Senão houver melhoria o contador é incrementado
				cont += 1

			# Retorna-se a melhor coloração encontrada
			return new_coloring
