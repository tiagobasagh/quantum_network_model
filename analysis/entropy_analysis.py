# default libreries
import math
# extearnal libraries
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

from tools import get_data

def shanon_entropy(p):
	return - p * math.log(p)


def calculate_entropy(name):
	historic_probability = get_data(name)
	historic_entropy = []
	for probability in historic_probability:
		s = 0
		N = int(probability[len(probability)-1])
		for i in range(len(probability)-1):
			s+= shanon_entropy(float(probability[i])/N)
		
		historic_entropy.append(s)

	return historic_entropy, math.log(N)

def plot_entropy(entropy_curves=[], labels=[], max_entropy=0, title='Entropy'):
		plt.figure(1)
		
		for s in range(len(entropy_curves)):
			plt.plot(entropy_curves[s], label= labels[s] )

		if len(entropy_curves) == 1:
			
			critical = critical_step(entropy_curves[0], max_entropy)
			plt.hlines(max_entropy, 0, len(entropy_curves[0]), 
			           colors='k', linestyles='dashed', label='Max entropy')
			plt.vlines(critical, 0, max_entropy, 
				       colors='r', linestyles='dashed', label=f'Critical connection: {critical}')
		
		
		plt.legend()
		plt.title(title)
		plt.show()


def search_critical_steps(name=[]):
	critical_steps = []

	for file in name:
		entropy,max_entropy = calculate_entropy(file)
		critical_steps.append(critical_step(entropy, max_entropy))

	return critical_steps

def critical_step(entropy, max_entropy):
	step = 0
	while(entropy[step] < max_entropy/4) and (step < (len(entropy)-2)):
		step+=1

	return step


