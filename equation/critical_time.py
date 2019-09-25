import math
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from solve_equation import get_critical_time

def conection2time(conection, size):
	return math.log(size) * conection/ size 

def time2conection(time, size):
	return size*time/math.log(size) 

def linear_function(x, m, b):
	return m*x  + b

def assintotic_limit(tc, ls_times):
	popt, pcov = curve_fit(linear_function, range(len(ls_times)), np.asarray(ls_times))
	plt.figure(1)
	plt.hlines(tc, 0, len(ls_times), linestyle='dashed', label=f'Numérico: {int(tc*100)/100}')
	#plt.hlines(tc-0.5, 0, len(ls_times), linestyle= 'dashdot', label=f'Simulaciones: {int((tc-0.5)*100)/100}')
	plt.plot(ls_times, 'o', label='Simulaciones ')
	plt.plot(range(len(ls_times)),  linear_function(np.asarray(ls_times), *popt), label=f'Simulacion: {popt[1]}' )
	plt.xlabel('tamaño red (N)/10000')
	plt.ylabel('tiempo crítico')
	plt.title('Tiempo crítico: Lambda 7')
	plt.legend()


def linear_relationship(ls_cc_sim, ls_cc_num, tipe, n):
	popt, pcov = curve_fit(linear_function, np.asarray(ls_cc_sim), np.asarray(ls_cc_num))
	plt.figure(2)
	plt.plot(ls_cc_sim, ls_cc_num, 'o', label=f'simulación vs numérico: {tipe}={n}')
	plt.plot(np.asarray(ls_cc_sim), 
		     linear_function(np.asarray(ls_cc_sim), *popt), 
		     'g--', label=f'Ajuste lineal: [Pendiente:{int(popt[0]*100)/100},  Origen:{int(popt[1]*100)/100}]')
	plt.xlabel('Conexión crítica [simulacion]')
	plt.ylabel('Conexión crítica [numérica]')
	plt.title('Conexión crítica: Relación entre los modelos')
	plt.legend()

def analysis_fix_size(ls_cc_sim, ls_size, lamda):
	tc = get_critical_time(lamda, 50)
	ls_cc_num = [time2conection(tc, size) for size in ls_size]
	ls_tc = [conection2time(ls_cc_sim[i], ls_size[i]) for i in range(len(ls_cc_sim))]


	assintotic_limit(tc, ls_tc)
	linear_relationship(ls_cc_sim, ls_cc_num, 'Lambda', lamda )

def analysis_fix_lamda(ls_cc_sim, ls_lambda, size):
	ls_tc = []
	for l in ls_lambda:
		ls_tc.append(get_critical_time(l, 50))

	ls_cc_num = [time2conection(tc, size) for tc in ls_tc]
	linear_relationship(ls_cc_sim, ls_cc_num, 'size', size)

#ls_cc_sim = [943, 1719, 2467, 3148, 3850, 4520, 5161, 5845, 6509, 7131, 7733, 8372, 9062, 9695, 10304, 10919, 11537, 12168]
#ls_size = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000]
#analysis_fix_size(ls_cc_sim, ls_size, 10)
#ls_cc_sim = [1718, 2053, 2478, 2801, 3160, 3561] #7
#ls_size = [4000, 5000, 6000, 7000, 8000, 9000] 
#analysis_fix_size(ls_cc_sim, ls_size, 7)

#ls_cc_sim = [40, 558, 1230, 1996, 2920, 3904, 4905, 6009, 7152, 7999]
#ls_lambda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#analysis_fix_lamda(ls_cc_sim, ls_lambda, 10000)

ls_cc_sim = [445, 981, 1622, 2398, 3190, 3988]
ls_lambda = [3, 4, 5, 6, 7, 8]
analysis_fix_lamda(ls_cc_sim, ls_lambda, 8000)
plt.show()

