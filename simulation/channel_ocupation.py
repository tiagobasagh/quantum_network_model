import networkx as nx 
import numpy as np


class ChannelOcupation:
	def __init__(self, G):
		self.G = G

	def remove_channel(self, list_path):
		for i_path in range(len(list_path)-1):
			e = (list_path[i_path],list_path[i_path+1])
			self.G.remove_edge(*e)

	def save_size_subgraphs(self):
		return list(nx.connected_component_subgraphs(self.G))

	def start_simulation(self, total_steps, name='heterodoxia'):
		steps = 0
		
		while steps<= total_steps: 
			node_1 = np.random.randint(1, len(self.G)) 
			node_2 = np.random.randint(1, len(self.G))

			if (node_1 !=node_2) and nx.has_path(self.G, node_1, node_2):
				self.remove_channel(nx.shortest_path(self.G, source=node_1, target=node_2))
				self.save_size_subgraphs(name)
				steps+=1
				if probability:
					self.save_frecuency(self.frecuency(), f'{name}_probability')

	def frecuency(self)
		sucefful = 0
		for i in range(10000):
			node_1 = np.random.randint(1, len(self.G)) 
			node_2 = np.random.randint(1, len(self.G))

			if (node_1 !=node_2) and nx.has_path(self.G, node_1, node_2):
				sucefful+=1 

		return sucefful/10000

	def save_frecuency():
		pass