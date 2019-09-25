import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 

from make_layout import make_layout_circle



def subplot_draw(pos_y, pos_x, index, G, pos, map_color, cmap, title):
	plt.subplot(100*pos_y + 10 *pos_x + index)
	plt.title(title)
	plt.axis('off')
	nx.draw_networkx(G, 
					 with_labels=False, 
					 #pos=pos, 
					 node_size=60, 
					 node_color=map_color,
					 cmap =cmap)

N = 600
lamda = [0.5, 1.5]
title = [f'Regimen subcritico: \n lambda={lamda[0]}', 
         f'Regimen supercritico: \n lambda = {lamda[1]}']

map_color = np.random.randint(1, 20, N).tolist()
pos = make_layout_circle(N, 4)
cmap = 'gnuplot'
plt.figure(1)
for l in range(len(lamda)):
	G = nx.erdos_renyi_graph(N, lamda[l]/N)
	subplot_draw(1, 2, (l+1), G, pos, map_color, cmap, title[l])

plt.show()