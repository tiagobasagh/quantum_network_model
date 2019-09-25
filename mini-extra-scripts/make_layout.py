import math 
import os

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def get_color_map(N):
	color_map = []
	for n in range(N):
		color_map.append(0)
	return color_map

def change_color_map (color_map, node):
	color_map[node]+=1
	return color_map

def make_layout_matrix(size):
	layout = {}
	for i in range(0,size):
		layout[i] = [int(i/10)%10 + (-1)**(i%2) *(1/20), i%10 ]
	return layout


def make_layout_tree_2(children, generations):
	layout = {}
	ancester_positions = []
	for g in range(1, generations+2):
		for c in range(children**(g-1), children**g):
			if (c-1)== 0:
				layout[c-1] = [0, generations-g]
				ancester_positions.append(0)
			else:
				z = children**g - children**(g-1)
				signo = ((-1)**c)  
				delta = 1/z
				padre = int((c-2)/children) 
				position = ancester_positions[padre] +  signo * delta
				layout[c-1] = [position, generations-g]
				ancester_positions.append(position)
	
	return layout


def make_layout_tree(children, generations):
	layout = {}
	ancester_positions = []
	ancester_positions.append(1)
	layout[0] = [1, generations]
	last_c = 0
	for g in range(1, generations+2):
		for c in range(1, children**g +1):
			delta = 1/children**g
			signo = (children * (1 + int((c-1)/children)) - (c+int(children/2)))
			ancester = int( (last_c +c-1)/children)
			position = ancester_positions[ancester]+ signo*delta
			layout[last_c + c] = [ position, generations-g]
			ancester_positions.append(position)
		last_c = last_c + c
	return layout


def make_layout_circle(N, spiral):
	layout = {}
	indice = 1
	layout[0] = [0, 0]
	for radio in range(1, int(N/spiral)+2):
		for r in range(radio*spiral):
			layout[indice] = [radio*2* np.cos(r/(radio*spiral) * 2*np.pi) ,radio*2* np.sin(r/(radio*spiral) * 2*np.pi)]
			indice+=1
	return layout


def make_layout_spiral(N, spiral):
	layout = {}
	indice = 1
	layout[0] = [0, 0]
	for radio in range(1, int(N/spiral)+2):
		for r in range(radio*spiral):
			layout[indice] = [indice* np.cos(r/(radio*spiral) * 2*np.pi) ,indice* np.sin(r/(radio*spiral) * 2*np.pi)]
			indice+=1
	return layout

"""
N = 1000
G = nx.erdos_renyi_graph(N, 10/N)
pos = make_layout_spiral(N, 5)
plt.figure(1)
plt.axis('off')
nx.draw_networkx(G, with_labels=False, pos=pos, node_size=20)
plt.show()
"""