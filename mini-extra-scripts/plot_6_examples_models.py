import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def add_plot(pos_y, pos_x, index, G, title):
	plt.subplot(100*pos_y + 10 *pos_x + index)
	
	plt.title(f'{title}')
	plt.axis('off')
	nx.draw_circular(G, 
		             with_labels=True, 
		             node_size=600,
		             node_color='red')

def is_empty(array):
	is_empty = False
	for i in array:
		if i==99:
			is_empty = True
	
	return is_empty

def get_random_dif_number(n, a, b):
	rn = n
	while rn==n:
		rn = np.random.randint(a,b)
	return rn

def make_dic_distribution(dist):
	dic = {}
	for i in range(len(dist)):
		dic[i]=[99]*dist[i]

	return dic

def make_conf_model(dist):
	try_again = True
	while try_again:
		count = 0
		try_again = False
		make_it = False
		G = nx.empty_graph(N)
		
		dist_dic = make_dic_distribution(dist)
		for node_1 in dist_dic:
			if is_empty(dist_dic[node_1]):
				for i in range(len(dist_dic[node_1])):			
					if dist_dic[node_1][i]==99:
						while not make_it:
							node_2 = get_random_dif_number(node_1, 0, len(dist))
							if (99 in dist_dic[node_2]) and not(node_1 in dist_dic[node_2]) and not(node_2 in dist_dic[node_1]):
								dist_dic[node_2][dist_dic[node_2].index(99)] = node_1
								dist_dic[node_1][i] = node_2
								G.add_edge(node_1, node_2)
								make_it = True
							if count>99:
								make_it = True
								try_again = True
							count+=1
					
					make_it = False
	
	return G, dist_dic

def distribution_model(G, N):
	index=1
	for i in range(N-1):
		for j in range(i+1, N):
			G.add_edge(i,j)
			add_plot(2, 3, index, G, f'{index} - G(4,1)')
			G.remove_edge(i,j)
			index+=1


N = 5
plt.figure(1)

plt.suptitle(f'Erdos-Renyi: {N} Nodos. P=0.5')
for i in range(1, 7):
	G = nx.erdos_renyi_graph(N, 0.5)
	add_plot(2, 3, i, G, '')
plt.show()
