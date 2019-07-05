
import math

import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

import entropy_analysis as ea
from tools import make_list_files


def fit_curve(curve, x, y):
	curves_dic = {'rational': rational_function,
	              'linear': linear_function,
	              'exponential': exponential_function}
	results = curve_fit(curves_dic[curve], x, y)

	return results

def exponential_function(x, A, lamda, b):
	return	A*np.exp(-lamda*x) + b

def rational_function(x, p, m, b):
	return (m/x**p) + b

def linear_function(x, m, b):
	return m*x  + b


"""
m = 0.09932262 
d = -0.29348214
p = 0.26254999 
k = 0.50749265 
b = 0.43652343
N = 10000
lamda = k/(m*(N/1000)**p) + (b-d)/m


f =  k/(N/1000)^p + b 
f = m * lamda + d 

m * lamda + d = k/(N/1000)^p + b

lamda = k/[m*(N/1000)^p] + (b-d)/M
"""

def fix_lamda(schema_files, inicial, final, intervalo, lamda):
	list_files = make_list_files(schema_files, inicial, final, intervalo)
	critical_steps = ea.search_critical_steps(list_files)

	y = []
	x = []
	
	for i in range(len(critical_steps)):
		y.append(critical_steps[i]/((i+1)*intervalo))
		x.append((i+1))

	#exp_popt, exp_pcov = fit_curve('exponential', x, y)
	rat_popt, rat_pcov = fit_curve('rational', x, y)
	print(rat_popt)
	plt.figure(1)
	plt.plot(x, y, 'ko', label='Simulation: Critial ratio(lamda)')
	#plt.plot(x, exponential_function(np.asarray(x), *exp_popt),  
	#	     'r-', label= 'Exponential:')

	plt.plot(x, rational_function(np.asarray(x), *rat_popt),  
		     'r-', label= f'Rational: m/x^p + b')

	plt.legend()
	plt.title('Configuration model: Critical Ratio vs Size')
	plt.xlabel('N/1000')
	plt.ylabel('Critical ratio')
	plt.show()

def fix_size(schema_files, inicial, final, intervalo, size):
	list_files = make_list_files(schema_files, inicial, final, intervalo)
	critical_steps = ea.search_critical_steps(list_files)
	
	y = []
	x = []
	
	for i in range(len(critical_steps)):
		y.append(critical_steps[i]/size)
		x.append( i*intervalo + inicial)
	

	popt, pcov = fit_curve('linear', x, y)
	print(pcov)
	plt.figure(1)
	plt.plot(x, y, 'ko', label='Simulation: Critial ratio(lamda)')
	plt.plot(x, linear_function(np.asarray(x), *popt),  
		     'r-', label= f'linear fit: ({int(1000*popt[0])/1000})x + ({int(1000*popt[1])/1000})')

	plt.legend()
	plt.title('Configuration model: Critical Ratio vs Lamda')
	plt.xlabel('Lamda')
	plt.ylabel('Critical ratio')
	plt.show()
	

