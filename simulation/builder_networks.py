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
