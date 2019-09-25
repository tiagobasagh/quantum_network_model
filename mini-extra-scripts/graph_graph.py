import math 
import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from make_layout import (make_layout_tree_2, 
	                     make_layout_circle, 
	                     get_color_map, 
	                     change_color_map,
	                     make_layout_tree,
	                     make_layout_spiral)


def population_tree(children, generations):
	N = 0
	for n in range(generations):
		N+=children**n

	return N

def list_subgraf(G):
	grafos = list(nx.connected_component_subgraphs(G))
	ls_subgraph = []
	for g in grafos:
		ls_subgraph.append(g.number_of_nodes())

	return ls_subgraph	

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

def draw_graph(n, G, pos, step, entropy, map_color, name_graph,  max_entropy):
	cmap = 'winter'
	#cmap = 'autumn'
	cmap = 'summer'
	#cmap= 'plasma'
	fig, ax = plt.subplots()
	plt.title(f' {name_graph} \n Successful connections: {step} \n Entropy: {int(100*entropy)/100} \n MaxEntropy: {int(100*max_entropy)/100}')
	plt.axis('off')
	nx.draw_networkx(G, 
		             with_labels=False, 
		             pos=pos, 
		             node_size=60, 
		             node_color=map_color, 
		             cmap =cmap)
	
	if n!=1:
		im = ax.scatter(color_map, color_map, c=color_map, cmap=cmap)
		fig.colorbar(im, ax=ax)
	

children = 6
generations = 3
N = population_tree(children, generations+1)
name_graph = 'Tree model'
G = nx.balanced_tree(children, generations)
max_entropy = calculate_entropy(np.ones(N), N)
pos = make_layout_tree(children, generations)

"""
name_graph = 'Erdos-Renyi Model'
N = 1000
G = nx.erdos_renyi_graph(N, 2/N)
pos = make_layout_spiral(N,7)
max_entropy = calculate_entropy(np.ones(N), N)
pos=make_layout_spiral(N, 3)
"""

"""
name_graph = 'Configuration Model - Poisson distribution'
N = 1000
lamda = 5
G = nx.configuration_model(np.random.poisson(lamda, N))
pos = make_layout_spiral(N, 7)
max_entropy = calculate_entropy(np.ones(N), N)
pos=make_layout_spiral(N, 3)
"""

"""

name_graph = 'Barabasi Albert Model'
N = 1000
lamda = 2
G = nx.barabasi_albert_graph(N, lamda)
pos = make_layout_spiral(N, 7)
max_entropy = calculate_entropy(np.ones(N), N)
pos=make_layout_spiral(N, 3)
"""


ready_4 = False
ready_2 = False
entropys = []
total_steps = 3
steps=1
color_map = get_color_map(N)

print(max_entropy)
draw_graph(1, G, pos, 0, 0, color_map, name_graph, max_entropy)

while steps<= total_steps:
	node_1 = np.random.randint(1, len(G)) 
	node_2 = np.random.randint(1, len(G))
	if (node_1 !=node_2) and nx.has_path(G, node_1, node_2):
		steps+=1
		G = remove_channel(G, nx.shortest_path(G, source=node_1, target=node_2))
		color_map = change_color_map(color_map,node_1)
		color_map = change_color_map(color_map,node_2)
		entropy = calculate_entropy(list_subgraf(G), G.number_of_nodes())
		
		if not ready_2 or not ready_4:
			if  not ready_2:
				print(f'2: {steps} with {entropy}')
				draw_graph(2, G, pos, steps, entropy, color_map, name_graph, max_entropy)
				ready_2 = True
			elif entropy>max_entropy/2 and not ready_4:
				print(f'3: {steps} with {entropy}')
				draw_graph(3, G, pos, steps, entropy, color_map, name_graph, max_entropy)
				ready_4 = True

print(f'4: {steps} with {entropy}')
draw_graph(4, G, pos, steps, entropy, color_map, name_graph, max_entropy)

plt.show()
