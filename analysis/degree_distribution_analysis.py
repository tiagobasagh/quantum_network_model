import math

import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit
from scipy.misc import factorial
from ast import literal_eval

from tools import get_data, make_empty_dict_of_list
from entropy_analysis import search_critical_steps

def poisson_function( k, lamda):
	return (np.exp(-lamda)* lamda**k)/factorial(k)

def raw2listdistribution( raw_data):
	poisson_curves = []
	degree_evolution = make_empty_dict_of_list(list(literal_eval(raw_data[0][0]).keys()))
	for i in range(len(raw_data)):
		aux_dict = literal_eval(raw_data[i][0])
		poisson_curves.append([])
		keys = list(aux_dict.keys())
		keys.sort()
		for k in keys:
			degree_evolution[k].append(aux_dict[k])
			poisson_curves[i].append(aux_dict[k])
	return degree_evolution, poisson_curves

def curve_of_params_fits(poisson_curves, N):

	N = 10000
	x = range(len(poisson_curves[0]))
	popt = []
	pcov = []
	for i in range(len(poisson_curves)):
		rat_popt, rat_pcov = curve_fit(poisson_function,
								  	   x,
								  	   np.asarray(poisson_curves[i])/N)
		popt.append(rat_popt)
		pcov.append(rat_pcov[0][0])

	return popt, pcov

def graph_degree_evolution(degree_evolution, tc):
	plt.figure(1)
	for k in degree_evolution.keys():
		if k in [0, 1, 2, 3, 4, 5]:
			plt.plot(degree_evolution [k], label=f'k: {k}')
		else:
			plt.plot(degree_evolution [k],'--')

	plt.vlines(tc, 0, 8000, linestyles='dashed', label='Conexión Crítica')
	plt.xlabel('Conexiones exitosas')
	plt.ylabel('Número de nodos')
	plt.legend()
	plt.title('Evolución del número de nodos de grado K')

def graph_curve_of_params(params, error, tc):

	plt.figure(2)
	plt.plot(params, label='Lambdas del ajuste poisson')
	#plt.errorbar(range(len(params)), params, yerr=error)
	plt.vlines(tc, 0, 5, linestyles='dashed', label='Conexión Crítica')
	plt.xlabel('Conexiones exitosas')
	plt.ylabel('Parámetro lambda')
	plt.legend()
	plt.title('Evolución parámetro lambda')

def multi_curves_distribution(curve_1, params_1, 
	                          curve_2, params_2, 
	                          curve_3, params_3, 
	                          curve_4, params_4):
	
	x =range(len(curve_1))
	plt.figure(3)
	plt.subplot(221)
	plt.plot(curve_1, 'o' ,label ='data')
	plt.plot(poisson_function(np.asarray(x), *params_1), label='ajuste')
	plt.legend()
	plt.title('Estado inicial de la red')

	plt.subplot(222)
	plt.plot(curve_2, 'o' ,label ='data')
	plt.plot(poisson_function(np.asarray(x), *params_2), label='ajuste')
	plt.title('Pre conexión crítica')
	plt.legend()

	plt.subplot(223)
	plt.plot(curve_3, 'o' , label ='data')
	plt.plot(poisson_function(np.asarray(x), *params_3), label='ajuste')
	plt.title('conexión crítica')
	plt.legend()

	plt.subplot(224)
	plt.plot(curve_4, 'o', label ='data')
	plt.plot(poisson_function(np.asarray(x), *params_4), label='ajuste')
	plt.title('Post conexión crítica')
	plt.legend()

	plt.suptitle(f'Distribución de grados para distintos tiempos')


N=10000

tc = search_critical_steps(['cm_5_10000'])[0]
raw_data = get_data('dist_cm_5_10000', delimiter='\n')
degree_evolution, poisson_curves = raw2listdistribution(raw_data)
params, error = curve_of_params_fits(poisson_curves, N)
graph_degree_evolution(degree_evolution, tc)
graph_curve_of_params(params, error, tc)

multi_curves_distribution(np.asarray(poisson_curves[0])/N, params[0],
						  np.asarray(poisson_curves[int(tc/2)])/N, params[int(tc/2)],
						  np.asarray(poisson_curves[int(tc)])/N, params[int(tc)],
						  np.asarray(poisson_curves[tc+100])/N, params[tc+100])

plt.show()


"""
#print(pcov)

"""
#plt.show()

"""
plt.figure(1)
plt.plot(np.asarray(poisson_curves[i])/N, label='data')
plt.plot(poisson_function(np.asarray(x), *rat_popt), label='ajust')
plt.plot(poisson_function(np.asarray(x), int(rat_popt)), label='ajust fix')
plt.plot()
plt.legend()
plt.show()
#print(a)
"""
"""

"""

"""

plt.figure(1)
for i in range(len(raw_data)):
	if i%50 == 0:
		plt.plot(poisson_curves[i])
	if i==7124:
		plt.plot(poisson_curves[i], label=f'paso numero {i}')		
plt.legend()
plt.show()

"""