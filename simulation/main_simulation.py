import math

from builder_networks import BuilderNetworks
from channel_ocupation import ChannelOcupation


# G = BuilderNetworks.tree_model(3,3)
N = 10000
e = 0
G = BuilderNetworks.erdos_renyi_model(size=N, probability=(1+e)*math.log(N)/N)
ChannelOcupation(G).start_simulation(9000, name=f'erdos_renyi_{N}', probability=False)