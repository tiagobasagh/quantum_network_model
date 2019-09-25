import matplotlib.pyplot as plt 
import numpy as np

import entropy_analysis as ea
from fit_analysis import fix_size, fix_lamda
from tools import make_list_files


def same_curve_plots_fix_N(schema_file, schema_label, N, min_lamda, max_lamda):
	s = []
	labels = []
	for i in range(min_lamda, max_lamda+1):
		entropy, max_entropy = ea.calculate_entropy(schema_file.format(i, N))
		s.append(entropy)
		labels.append(schema_label.format(i))

	ea.plot_entropy(s, labels, max_entropy, title = 'Entropy')


def same_curve_plots_fix_L(schema_file, schema_label, lamda, N_min, N_max):
	s = []
	labels = []
	for i in range(N_min, N_max+1000, 1000):
		entropy, max_entropy = ea.calculate_entropy(schema_file.format(lamda, i))
		s.append(entropy)
		labels.append(schema_label.format(i))

	ea.plot_entropy(s, labels, max_entropy, title = 'Entropy')


"""
plt.figure(1)
s = []
labels=[]

entropy, max_entropy = ea.calculate_entropy('erdos_reny_10_10000')
s.append(entropy)
label = 'p =5/10000'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=311)

entropy, max_entropy = ea.calculate_entropy('erdos_reny_10_10000')
s.append(entropy)
label = 'p =10/10000'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=312)

entropy, max_entropy = ea.calculate_entropy('erdos_reny_10_10000')
s.append(entropy)
label = 'p =15/10000'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=313)

plt.suptitle(f'IN PROGRESS ....')
plt.show()
"""