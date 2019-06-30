import entropy_analysis as ea
import matplotlib.pyplot as plt 

"""
schema_file = 'cm_poisson_10_{}'
list_files = ea.make_list_files(schema_file, 1000, 12000, 1000)
critical_steps = ea.search_critical_steps(list_files)
print(critical_steps)
"""
"""
s = []
labels = []
entropy, max_entropy = ea.calculate_entropy('cm_poisson_10_11000')
s.append(entropy)
labels.append('wachin')
ea.plot_entropy(s, labels, max_entropy)
"""


""" 
Quiero ver entonces como varia el step_critica en funcion del tamaño de la poblacion. 
Esto deberia tender, en algun momento en algun ratio. 

Grafico entonces: step_crito vs poblacion o step_critico/poblacion vs poblacion
"""

l = [0.943, 0.8595, 0.8223333333333334, 0.787, 0.77, 0.7533333333333333, 0.7372857142857143, 0.730625, 0.7232222222222222, 0.7131, 0.703]

plt.figure(1)
plt.plot(l)
plt.show()