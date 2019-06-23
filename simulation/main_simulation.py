from builder_networks import BuilderNetworks
from channel_ocupation import ChannelOcupation

# G = BuilderNetworks.tree_model(3,3)
G = BuilderNetworks.erdos_renyi_model(size=10, probability=0.5)
ChannelOcupation(G).start_simulation(2, name='Test', probability=True)