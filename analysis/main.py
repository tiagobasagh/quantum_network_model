import entropy_analysis as ea
s = []
labels = []
entropy, max_entropy = ea.calculate_entropy('cm_poisson_10_8000')
s.append(entropy)
labels.append('wachin')
ea.plot_entropy(s, labels, max_entropy)



""" 
Quiero ver entonces como varia el step_critica en funcion del tamaño de la poblacion. 
Esto deberia tender, en algun momento en algun ratio. 

Grafico entonces: step_crito vs poblacion o step_critico/poblacion vs poblacion
"""