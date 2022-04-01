import math

import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

import entropy_analysis as ea
from tools import make_list_files


def fit_curve(curve, x, y):
	""" """
	curves_dic = {'rational': rational_function,
	              'linear': linear_function,
	              'exponential': exponential_function}
	
	results = curve_fit(curves_dic[curve], x, y)

	return results

def poisson_function(k, lamda):
	return (np.exp(-lamda)* lamda**k)/math.factorial(k)

def exponential_function(x, A, lamda, b):
	""" """
	return	A*np.exp(-lamda*x) + b


def rational_function(x, b, m):
	""" """
	return (m/x**0.65) + b


def linear_function(x, m, b):
	""" """
	return m*x  + b


def fix_lamda(schema_files, inicial, final, intervalo, lamda):
	""" """
	list_files = make_list_files(schema_files, inicial, final, intervalo)
	critical_steps = ea.search_critical_steps(list_files)

	y = []
	x = []
	
	for i in range(len(critical_steps)):
		y.append(critical_steps[i])
		x.append(i*intervalo + inicial)

	print(y)
	print(x)

	plt.plot(x, y, 'o', label=f'Lambda {lamda}')
	plt.legend()
	plt.title('Modelo de configuraciones: Tamaño variable.')
	plt.xlabel('Tamaño de la red')
	plt.ylabel('Conexion crítica')


def fix_size(schema_files, inicial, final, intervalo, size):
	""" """
	list_files = make_list_files(schema_files, inicial, final, intervalo)
	critical_steps = ea.search_critical_steps(list_files)
	
	y = []
	x = []
	
	for i in range(len(critical_steps)):
		#y.append(np.log(size)*critical_steps[i]/size)
		y.append(critical_steps[i])
		x.append( i*intervalo + inicial)
	

	print(y)
	print(x)
	
	plt.plot(x, y, 'o', label=f'Tamaño de la red: {size}') 

	plt.legend()
	plt.title('Modelo de configuraciones: Lambda variante.')
	plt.xlabel('Lambda')
	plt.ylabel('Conexion crítica')
