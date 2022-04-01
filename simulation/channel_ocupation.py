 
import networkx as nx 
import numpy as np

from builder_networks import BuilderNetworks
from config import stored_path
from tools import list2dict, clean_dict

class ChannelOcupation:
	def __init__(self, G):
		self.G = G

	def remove_channel(self, list_path):
		for i_path in range(len(list_path)-1):
			e = (list_path[i_path],list_path[i_path+1])
			self.G.remove_edge(*e)

	def get_degree_distribution(self, degree_dict):
		degree_dict = degree_dict 
		for degree in dict(self.G.degree()).values(): 
			degree_dict[degree]+=1

		return degree_dict

	def save_distribution(self, name, degree_dict):
		degree_dict = self.get_degree_distribution(degree_dict)
		f=open(f'{stored_path.format(f"dist_{name}")}',"a")
		f.write(f'{degree_dict}\n')

	def save_size_subgraphs(self, name):
		size_subgraphs = list(nx.connected_component_subgraphs(self.G))
		
		f=open(f'{stored_path.format(name)}',"a")
		for subG in size_subgraphs:
			f.write(f'{subG.number_of_nodes()},')

		f.write(f'{self.G.number_of_nodes()}\n')
		f.close()

	def start_simulation(self, total_steps, name='results', savedegree=False):
		""" 
		Función principal de la simulacion. Guarda el tamaño de los subgrafos conexos que aparecen
		a medida que se van ocupando los canales de ocupacion.

		:params int total_steps: total de conexiones que se quieran realizar. 
		:params string name: Nombre del archivo generado con los datos de la evolucion. 
							 Por default es 'results'
		:params boolean savedegree: Si es True ademas de los datos esperados, guardo la distrubición 
		                            de los nodos en cada dado instante. Por default es False. 
		                            Tener en cuenta que aunmenta los tiempos propios de la simulación.
		
		Ejemplo de uso:

		ChannelOcuppation(G).start_similatiom()

		donde G es un objeto de la liberia Networkx [https://networkx.github.io/]
		"""
		steps = 0
		self.save_size_subgraphs(name)
		if savedegree:
			degree_dict = list2dict(list(set(dict(self.G.degree()).values())))
			self.save_distribution(name, degree_dict)
		
		while steps<= total_steps: 
			node_1 = np.random.randint(1, len(self.G)) 
			node_2 = np.random.randint(1, len(self.G))

			if (node_1 !=node_2) and nx.has_path(self.G, node_1, node_2):
				self.remove_channel(nx.shortest_path(self.G, source=node_1, target=node_2))
				self.save_size_subgraphs(name)
				if savedegree:
					self.save_distribution(name, degree_dict)
					egree_dict = clean_dict(degree_dict, 0)
				steps+=1
	