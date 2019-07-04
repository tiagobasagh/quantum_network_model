import entropy_analysis as ea
import matplotlib.pyplot as plt 

from tools import make_list_files




def fix_lamda(schema_files, lamda, size):
	list_files = make_list_files(schema_file, 1000, size, 1000)
	critical_steps = ea.search_critical_steps(list_files)
	critical_ratio = []
	for i in range(len(critical_steps)):
		critical_ratio.append(critical_steps[i]/((i+1)*10000))

	print(critical_ratio)
	plt.figure(1)
	plt.plot(critical_ratio, 'o')
	plt.show()


def fix_size(schema, N, max_lamda):
	s = []
	labels = []
	for i in range(4, max_lamda+1):
		entropy, max_entropy = ea.calculate_entropy(schema.format(i, N))
		s.append(entropy)
		labels.append(f'Possion: Lamda ={i}')

	ea.plot_entropy(s, labels, max_entropy, title = 'Entropy')


schema_file = 'cm_poisson_10_{}'
fix_lamda(schema_file, 10, 19000)

#fix_size('lamda_cm_poisson_{}_{}', 10000, 10)
#s = []
#labels = []

#entropy, max_entropy = ea.calculate_entropy('cm_poisson_10_10000')
##s.append(entropy)
#labels.append('Possion distribution: Lamda=10 ')

#entropy, max_entropy = ea.calculate_entropy('lamda_cm_poisson_10_10000')
#s.append(entropy)
#labels.append('poisson 3')

#ea.plot_entropy(s, labels, max_entropy, title = 'Connectivity Entropy: configuration-model network')



""" 
Quiero ver entonces como varia el step_critica en funcion del tamaño de la poblacion. 
Esto deberia tender, en algun momento en algun ratio. 

Grafico entonces: step_crito vs poblacion o step_critico/poblacion vs poblacion
"""

