# default libreries
import math
# extearnal libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from tools import get_data

def shanon_entropy(p):
	""" """
	return - p * math.log(p)


def calculate_entropy(name):
	""" 
	Función que devuelve la curva de entropia de una dada simulacion (../simulation/channel_ocupation.py)
	Para ello levanto un archivo guardado en../stored/{name}.csv, en el cual cada estado de la red
	genera una fila, donde cada elemento de la fila representa un subgrafo y el numero el tamaño 
	de ese subgrafo. Un ejemplo:
	{estado inicial} 1000 \n
	{1} 999, 1 \n
	{2} 997, 1 , 2 \n
	     .
	     .
	     .
	{final} 1, 1, 1, 1, ..., 1, 1, 1 

	:param string name: Nombre del archivo con los datos entregados por la simulación. 

	:return list historic_entropy: Lista con los valores de la curva de entropia. 
	"""
	historic_probability = get_data(name)
	historic_entropy = []
	for probability in historic_probability:
		s = 0
		N = int(probability[len(probability)-1])
		for i in range(len(probability)-1):
			s+= shanon_entropy(float(probability[i])/N)
		
		historic_entropy.append(s)

	return historic_entropy, math.log(N)


def plot_entropy(entropy_curves=[], labels=[], max_entropy=0, x_range=[], title='Entropy', pos=111):
		""" """
		plt.subplot(pos)
		for s in range(len(entropy_curves)):
			x_range = list(range(1,len(entropy_curves[s])+1))
			#color = np.random.choice(np.arange(0,1,0.001), size=3)
			color = '#36355b'
			plt.plot(x_range, 
				     entropy_curves[s], 
				     label= labels[s]
				     )

		if len(entropy_curves) == 1:
			
			critical = critical_step(entropy_curves[0], max_entropy)
			plt.hlines(max_entropy, 0, 17700, 
			         colors='#8789ae', linestyles='dashed', label=f'Entropía Máxima: {int(100*max_entropy)/100}')
			plt.vlines(x_range[critical], 0, max_entropy, 
				       colors='#ff633d', linestyles='dashed', label=f'Probabilidad crítica: {critical+1}')
		
		if not (pos==311 or pos==312):
			plt.xlabel('P')	
		
		plt.ylabel('Entropía')
		plt.legend(loc='best')
		if pos==111: 
			plt.title(title)


def search_critical_steps(name=[]):
	""" """
	critical_steps = []

	for file in name:
		entropy,max_entropy = calculate_entropy(file)
		critical_steps.append(critical_step(entropy, max_entropy))

	return critical_steps

def critical_step(entropy, max_entropy):
	""" """
	step = 0
	while(entropy[step] > max_entropy/4) and (step < (len(entropy)-2)):
		step+=1
	return step


