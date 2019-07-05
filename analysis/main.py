import matplotlib.pyplot as plt 

import entropy_analysis as ea
from fit_analysis import fix_size, fix_lamda
from tools import make_list_files


"""
ME PERMITE PLOTEAR VARIOS GRAFICOS DEL MISMO TIPO DE UNA
def fix_size(schema_file, schema_label, N, min_lamda, max_lamda):
	s = []
	labels = []
	for i in range(min_lamda, max_lamda+1):
		entropy, max_entropy = ea.calculate_entropy(schema_file.format(i, N))
		s.append(entropy)
		labels.append(schema_label.format(i))

	ea.plot_entropy(s, labels, max_entropy, title = 'Entropy')

schema_file = 'lamda_cm_poisson_{}_{}'
schema_label = 'Lamda = {}'
fix_size (schema_file, schema_label, 10000, 4, 11)
"""

#schema_file = 'lamda_cm_poisson_{}_10000'
#fix_size(schema_file, 4, 12, 1, 10000)


schema_file = 'cm_poisson_10_{}'
fix_lamda (schema_file, 1000, 18000, 1000, 10)
