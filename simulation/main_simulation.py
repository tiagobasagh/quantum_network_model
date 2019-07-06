import math

from builder_networks import BuilderNetworks
from channel_ocupation import ChannelOcupation

def fix_lamda(lamda, N_min, N_max, intervalo):
	for i in range(N_min, N_max+ intervalo, intervalo):
		G = BuilderNetworks.configuration_model(i, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(i * 0.8) , 
			                                 name=f'cm_poisson_{lamda}_{i}', 
			                                 probability=False)

def fix_N(N, lamda_min, lamda_max, intervalo):
	for i in range(lamda_min, lamda_max + intervalo, intervalo):
		G = BuilderNetworks.configuration_model(N, i) # poisson por defecto
		print(int(N * (i/10)))
		ChannelOcupation(G).start_simulation( int(N * (i/10) ), 
			                                 name=f'fix_N_cm_poisson_{i}_{N}', 
			                                 probability=False)

#lamda = 7
#N_min = 6000
#N_max = 18000
#fix_lamda(lamda, N_min, N_max, 1000)


#N= 8000
#lamda_min = 5
#lamda_max = 11
#fix_N(N, lamda_min, lamda_max, 1)



"""
def fix_N(lamda_max, N):
	for lamda in range(9, lamda_max+1):
		G = BuilderNetworks.configuration_model(N, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(N * 0.8) , 
			                                 name=f'lamda_cm_poisson_{lamda}_{N}', 
			                                 probability=False)


def repeat(lamda, N):
	for i in range(10):
		G = BuilderNetworks.configuration_model(N, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(N * 0.75) , 
			                                 name=f'lamda_cm_poisson_{lamda}_{N}_{i}', 
			                                 probability=False)
lamda = 12
N = 10000
G = BuilderNetworks.configuration_model(N, lamda)
ChannelOcupation(G).start_simulation(int(N) , 
		                             name=f'lamda_cm_poisson_{lamda}_{N}', 
		                             probability=False)
"""

"""
G = BuilderNetworks.tree_model(2, 13)
ChannelOcupation(G).start_simulation(2000, 
		                             name=f'tree_2_13', 
		                             probability=False)

G = BuilderNetworks.tree_model(3, 9)
ChannelOcupation(G).start_simulation(5000, 
		                             name=f'tree_3_9', 
		                             probability=False)
"""
G = BuilderNetworks.barbaresi_model(10000, 5)
ChannelOcupation(G).start_simulation(10000, 
		                             name=f'bar_5_10000', 
		                             probability=False)

