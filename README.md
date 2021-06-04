# Heuristic-Abduction-vns-vnd
Projeto desenvolvido na disciplina de Metaheuristica comparando o desempenho do algoritmo VSP VNS e um terceiro algoritmo(Heuristica) de nossa escolha. O terceiro algoritmo foi denominado Abduction e foi construído pelo próprio Grupo.

#ABDUCTION 
* O problema selecionado foi o problema de coloração de grafos.
* Solução dada pelo algoritmo ABDUCTION: Sugerida pela aluna Rafaela Martins, a heurística denominada Abduction  começa com uma lista ordenada por grau, com todos os vértices presentes no grafo. Inicialmente se retira o vértice de maior grau entre todos os demais. Feito isso, adiciona-se uma flag de colorido e atribui-se a menor cor possível aquele vértice e o elimina da lista.
Feito isso, retira-se todos os seus adjacente da lista ordenada e atribui-se esses adjacentes a uma outro lista chamada de “temporária”, além disso as flags de todos os adjacentes retirados mudam para visitados. Se a lista não estiver vazia, o algoritmo segue retirando e colorindo os vértices de maior grau. [Fonte Desenvolvida pelo próprio autor]
