
import networkx as nx 
import numpy as np

from builder_networks import BuilderNetworks
from config import stored_path

class ChannelOcupation:
	def __init__(self, G):
		self.G = G

	def remove_channel(self, list_path):
		for i_path in range(len(list_path)-1):
			e = (list_path[i_path],list_path[i_path+1])
			self.G.remove_edge(*e)

	def save_size_subgraphs(self, name):
		size_subgraphs = list(nx.connected_component_subgraphs(self.G))
		
		f=open(f'{stored_path.format(name)}',"a")
		for subG in size_subgraphs:
			f.write(f'{subG.number_of_nodes()},')

		f.write(f'{self.G.number_of_nodes()}\n')
		f.close()

	def start_simulation(self, total_steps, name='heterodoxia', probability=False):
		steps = 0
		
		while steps<= total_steps: 
			node_1 = np.random.randint(1, len(self.G)) 
			node_2 = np.random.randint(1, len(self.G))

			if (node_1 !=node_2) and nx.has_path(self.G, node_1, node_2):
				self.remove_channel(nx.shortest_path(self.G, source=node_1, target=node_2))
				self.save_size_subgraphs(name)
				steps+=1
				if probability:
					self.frecuency(f'{name}_frecuency')

	
	def frecuency(self, name):
		sucefful = 0
		for i in range(10000):
			node_1 = np.random.randint(1, len(self.G)) 
			node_2 = np.random.randint(1, len(self.G))

			if (node_1 !=node_2) and nx.has_path(self.G, node_1, node_2):
				sucefful+=1 

		f=open(f'{stored_path.format(name)}',"a+")
		f.write(f'{sucefful/10000 } \n')
		f.close()
