import matplotlib.pyplot as plt 

import entropy_analysis as ea
from fit_analysis import fix_size, fix_lamda
from tools import make_list_files



def same_curve_plots(schema_file, schema_label, N, min_lamda, max_lamda):
	s = []
	labels = []
	for i in range(min_lamda, max_lamda+1):
		entropy, max_entropy = ea.calculate_entropy(schema_file.format(i, N))
		s.append(entropy)
		labels.append(schema_label.format(i))

	ea.plot_entropy(s, labels, max_entropy, title = 'Entropy')

#schema_file = 'lamda_cm_poisson_{}_{}'
#schema_label = 'Lambda = {}'
#same_curve_plots(schema_file, schema_label, 10000, 4, 10)



s = []
labels = []




entropy, max_entropy = ea.calculate_entropy('tree_2_13')
s.append(entropy)
labels.append('Tree(3, 9)')

entropy, max_entropy = ea.calculate_entropy('tree_3_9')
s.append(entropy)
labels.append('Tree(2,13) ')

entropy, max_entropy = ea.calculate_entropy('lamda_cm_poisson_7_10000')
s.append(entropy)
labels.append('Configuration: Poisson distribution(10000, 7)')
"""
entropy, max_entropy = ea.calculate_entropy('cm_equi_1_15_9000')
s.append(entropy)
labels.append('Configuration: Unif-distribution(9000, 1,15)')

entropy, max_entropy = ea.calculate_entropy('erdos_renyi_10000')
s.append(entropy)
labels.append('Erdos-Reny(10000, 0.0001)')

entropy, max_entropy = ea.calculate_entropy('bar_5_10000')
s.append(entropy)
labels.append('Barabasi(10000, 3)')
"""
ea.plot_entropy(s, labels, max_entropy, title = 'Entropy curves to diferent models')

#schema_file = 'fix_N_cm_poisson_{}_8000'
#fix_size(schema_file, 3, 9, 1, 12000)
"""
[ 0.09932262 -0.29348214]
[[ 3.85566363e-06 -2.89174772e-05]
 [-2.89174772e-05  2.37123314e-04]]"""


#schema_file = 'cm_poisson_7_{}'
#fix_lamda (schema_file, 4000, 10000, 1000, 7)
"""
[p, m, b]
[[ 0.0004086  -0.00050421  0.00053431]
 [-0.00050421  0.00064202 -0.00067142]
 [ 0.00053431 -0.00067142  0.00070644]]"""