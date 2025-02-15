import networkx as nx 
import numpy as np 

class BuilderNetworks:

	def erdos_renyi_model(size, probability):
		return nx.erdos_renyi_graph(size, probability)

	def configuration_model(size, scale, name='poisson', loc=None):
		""" """
		distribution = [3]

		while not(sum(distribution)%2 == 0):
			distribution = make_distribution(size, scale, name, loc)
			"""mirar bien power distribution"""

		return nx.configuration_model(distribution)

	def tree_model(children, generations):
		return nx.balanced_tree(children, generations)

	def barbaresi_model(size,algo):
		return nx.barabasi_albert_graph(size, algo)

	def unbalanced_tree(lamda, generations):
		G = nx.empty_graph(1)
		for g in range(generations):
			if g == 0:
				childrens = np.random.poisson(lamda,1).tolist()[0]
				print(childrens)
				G = add_sons(G, 0, childrens, G.number_of_nodes())
				before_generation = 1
				
			else:
				actual_size = G.number_of_nodes()
				for n in range(before_generation, actual_size):
					childrens = np.random.poisson(lamda,1).tolist()[0]
					G = add_sons(G, n, childrens, G.number_of_nodes())	
					print(childrens)
				before_generation = actual_size

		return G



def make_distribution(size, scale, name, loc=None):
	dic_distributions = {'poisson': np.random.poisson,
	                     'power': np.random.power,
	                     'normal': np.random.normal,
	                     'exponential': np.random.exponential,
	                     'equi': np.random.randint}

	if loc:
		distribution = dic_distributions[name](loc, scale, size)
	else:
		distribution = dic_distributions[name](scale, size)

	return distribution.tolist()


def add_sons(G, nodo, childrens, actual_size):
		for i in range(childrens):
			G.add_node(actual_size + i)
			G.add_edge(nodo, actual_size + i)

		return G 
