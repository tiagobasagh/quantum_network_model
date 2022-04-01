import os

import networkx as nx
import numpy as np

project_path = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
stored_path = os.path.join(project_path,'stored/{}.csv')


def save_size_subgraphs(G, name):
		size_subgraphs = list(nx.connected_component_subgraphs(G))
		
		f=open(f'{stored_path.format(name)}',"a")
		for subG in size_subgraphs:
			f.write(f'{subG.number_of_nodes()},')

		f.write(f'{G.number_of_nodes()}\n')
		f.close()

size = 20000
for i in np.arange(0, 5, 0.002):
	print(i)
	G = nx.erdos_renyi_graph(size, i/size)
	save_size_subgraphs(G,'05_pt_er_20000')