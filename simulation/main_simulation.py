import math

from builder_networks import BuilderNetworks
from channel_ocupation import ChannelOcupation

def fix_lamda(lamda, N, intervalo):
	for i in range( 11000, N , intervalo):
		G = BuilderNetworks.configuration_model(i, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(i * 0.8) , 
			                                 name=f'cm_poisson_{lamda}_{i}', 
			                                 probability=False)

def fix_N(lamda_max, N):
	for lamda in range(1, lamda_max+1):
		G = BuilderNetworks.configuration_model(N, lamda) # poisson por defecto
		ChannelOcupation(G).start_simulation( int(N * 0.8) , 
			                                 name=f'cm_poisson_{lamda}_{N}', 
			                                 probability=False)


# G = BuilderNetworks.tree_model(3,3)
N = 16000
intervalo = 1000
e = 0
fix_lamda(10, N, intervalo)
#G = BuilderNetworks.erdos_renyi_model(size=N, probability=(1+e)*math.log(N)/N)
#G = BuilderNetworks.configuration_model(N, 10) # poisson por defecto
#ChannelOcupation(G).start_simulation(9000, name=f'cm_poisson{N}', probability=False)