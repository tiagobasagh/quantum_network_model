import math

from builder_networks import BuilderNetworks
from channel_ocupation import ChannelOcupation

def fix_lamda(lamda, N, intervalo):
	for i in range( 16000, N , intervalo):
		G = BuilderNetworks.configuration_model(i, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(i * 0.8) , 
			                                 name=f'cm_poisson_{lamda}_{i}', 
			                                 probability=False)

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
#G = BuilderNetworks.tree_model(3,3)

#repeat(10, 10000)


"""
N = 20000
intervalo = 1000
e = 0
fix_lamda(10, N, intervalo)
"""

#N = 10000
#lamda_max=15
#fix_N(lamda_max, N)

N = 18000
lamda = 10
G = BuilderNetworks.configuration_model(N, lamda)
ChannelOcupation(G).start_simulation((N*0.7), name=f'erdos_reny)_10_{N}', probability=False)

#G = BuilderNetworks.configuration_model(N, 10) # poisson por defecto
