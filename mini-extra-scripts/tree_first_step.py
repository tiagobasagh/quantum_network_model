import math
import os


import networkx as nx
import numpy as np

project_path = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
stored_path = os.path.join(project_path,'stored/{}.csv')


def remove_channel(G, list_path):
		for i_path in range(len(list_path)-1):
			e = (list_path[i_path],list_path[i_path+1])
			G.remove_edge(*e)
		return G

def shanon_entropy(p):
	""" """
	return - p * math.log(p)

def calculate_entropy(ls_subgraph, N):
	""" """
	s=0
	for size in ls_subgraph:
		s+= shanon_entropy(float(size)/N)
		

	return s


children = 2
generations = 13
entropys = []
for i in range(0, 10000):
	print(i)
	G = nx.balanced_tree(children, generations)
	for steps in range(0,2):
		node_1 = np.random.randint(1, len(G)) 
		node_2 = np.random.randint(1, len(G))
		if nx.has_path(G, node_1, node_2):
			G = remove_channel(G, nx.shortest_path(G, source=node_1, target=node_2))
			grafos = list(nx.connected_component_subgraphs(G))
			ls_subgraph = []
			for g in grafos:
				ls_subgraph.append(g.number_of_nodes())

	entropys.append(calculate_entropy(ls_subgraph, G.number_of_nodes()))

print(entropys)
print(sum(entropys)/len(entropys))
