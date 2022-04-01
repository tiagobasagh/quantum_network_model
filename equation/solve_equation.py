"""
This module is a collection is tools to resolve a particular 
differential equation, no pretend be more of that.

The equation system to descibre la dynamic of the system is: 
	d(mu)/dt = (k+1)(k+2) mu(k+2) - (k)(k-1) mu(k)
And may be write in matritial format as: 
	mu' = A mu 
where mu' and mu are vector and A is a matrix with coeficients (k+1)(k+2) and k(k-1)

to more information please see: []
"""

import math 
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

from utils import make_vec_poisson, linear_function, emptylist



def original_matrix(size):
	"""
	Build de matrix that describe the diferential equation.
    """
	M = np.zeros((size, size))
	for i in range(0, size):
		if not i in (0, 1):
			M[i,i] = a_value(i)
		
		if i < size-2:
			M[i,i+2] = b_value(i)
	return M

def a_value(k):
	"""
	Diagonal coeficient of the matrix. 
	"""
	return -k*(k-1)

def b_value(k):
	"""
	Unique coeficients [k, k+2] non zero outside diagonal. 	
	"""
	return (k+1)*(k+2)


def mu_tau(tau, solution, self_value, self_vector):	
	""" 
	calculation of mu(tau)
	"""
	mu = []
	for i in range(len(solution)):
		aux_mu = 0
		for k in range(len(solution)):
			aux_mu += self_vector[i][k] *  solution[k] * np.exp(self_value[k]*tau)
		
		mu.append(aux_mu) 

	return mu

def function_lambda(mu):
	"""
	Calculate lambda value using: 
		\lambda = \SUM_{i=1}^N \mu_i
	where M is the longitud of mi vector mu.
	
	:param ls mu: 
	"""

	lamda = 0
	for i in range(len(mu)):
		lamda += i * mu[i]
	return lamda 

def nu_tau(mu):
	"""

	"""
	lamda = function_lambda(mu)
	p = 0
	for i in range(len(mu)):
		p += i*(i-1)* mu[i]

	return p/lamda


def solve_equation(lamda, size):
	"""
	:param int lamda: define the poission distribution around lamda. 
	:param int size: Numbero of vector i want to solve the matritial equation.
	
	:return list solution: Solution of the differential equation. 
	:return list eigen_values: eigen values of matrix that describe the problem
	:return list eigen_vectors: eigen vectors of matriax that describe the problem.
	"""
	M = original_matrix(size) # Get (and create) matrix.
	eigen_values, eigen_vectors = np.linalg.eig(M) # Give eigen vuale, eigen vector of M.
	v_poisson = make_vec_poisson(lamda, size) 
	solution = np.linalg.solve(eigen_vectors, v_poisson) 
	
	print(eigen_vectors)
	return solution, eigen_values, eigen_vectors

def mu_evolution(lamda, size, dtau):
	"""
	"""
	mu_matrix_evolution = emptylist(size)
	solution, self_values, self_vector = solve_equation(lamda, size)
	
	for tau in np.arange(0, 3, dtau):
		mu = mu_tau(tau, solution, self_values, self_vector)
		for i in range(0, size):
			mu_matrix_evolution[i].append(mu[i])

	return mu_matrix_evolution

def rescalingtime(mus, dtau):
	""" 
	:param numpy.array object mus: 
	:param float dtau:

	:return list t: 
	:return float t_c:

	"""
	t = []
	t_c = 0
	t_aux = 0
	for i in range(len(mus[0])):
		mu = []
		for mu_k in mus:
			mu.append(mu_k[i])

		nu = nu_tau(mu)
		if nu>1:
			fl = function_lambda(mu)
			dt = tau2time(fl, nu, dtau)
			t_aux += dt 
			t_c = t_aux
		else:
			t_aux += dt 
		t.append(t_aux)
	return t, t_c

def tau2time(l , nu, tau):
	"""
	trasform tau value in t value, to rescale the problem. 
	:param int:
	:param float l: function lamda 
	:param float: 

	:return float: time value. 
	"""
	return  tau * ((nu-1) * l +1)/(math.log(math.exp(1), nu))


def plot_mus(lamda, size, dtau, rescaling=True):

	mus = mu_evolution(lamda, size, dtau)
	tau =  np.arange(0, 3, dtau)	
	t_c = 0

	if rescaling:
		t, t_c = rescalingtime(mus, dtau)
		type_time = 't(u.a.)'
	else:
		t = tau
		t_c = get_critical_value(lamda, size, time=False, timetau=True)
		type_time = 'tau(u.a)'
	
	for i in range(len(mus)):	
		if i in [0, 1, 2, 3, 4, 5, 10, 15]:
			plt.plot(t, mus[i], label=f'mu(k={i})')
		else:
			plt.plot(t, mus[i])

	plt.vlines(t_c, 0, 0.5, linestyles='dashed', label= f'crítico: {int(100*(t_c))/100}')

	plt.xlabel(type_time)
	plt.ylabel('ratio nodos')
	plt.title(f'Límite de grafo grande: Distribución de grados (k={lamda})')
	plt.legend()


def get_critical_value(k, size, dtau=0.001, time=True, timetau=False):
	"""
	Funcion que resuelve el sistema de ecuaciones dado por: 
		d(mu)/dt = (k+1)(k+2) mu(k+2) - (k)(k-1) mu(k)

	y devuelve el tiempo critica en el cual este se desconecta. 

	:params int k: Valor esperado para generar una distribucion de Poisson.
	:params int size: Valor que indica hasta que grado de nodos sera considerado. 
					  Si size=10, dentro de la resolución no considerar nodos de grado 11 o mayor. 
	:params float dtau: longitud de los pasos tau a darse. 
	:params boolean time: True por defualt. Si es True, la función devuelve t_crítico.
	:params boolean tau: False por default. Si es True, la función devuelve tau_critico.

	:return float t_c: tiempo crítico en el cual la red cambia sus propiedades. 
	:return float tau_c: tau crítico en el cual la red cambia sus propiedades.

	ejemeplo
	t, tau = get_critical_value(10, 40, dtau=0.01, time=True, timetau=True)

	"""
	tau = 0
	t_c = 0
	nu = 9999
	
	solution, eige_values, eige_vectors = solve_equation(k, size)
	while nu > 1:
		mu = mu_tau(tau, solution, eige_values, eige_vectors)
		nu = nu_tau(mu)
		lamda = function_lambda(mu)
		t_c+= tau2time(lamda, nu, dtau) 
		tau+=dtau
	
	if (time and timetau):
		return t_c, tau
	elif timetau:
		return tau

	else:
		return t_c


def time_of_k(max_k, size):
	ls_t = []
	ls_k = range(2, max_k+1)
	ls_tau = []
	for k in ls_k: 
		t, tau = get_critical_value(k, size, time=True, timetau=True)
		ls_t.append(t)
		ls_tau.append(tau)

	
	plt.figure(2)
	plt.plot(ls_k, ls_tau, 'co', label='')
	plt.xlabel('Poisson')
	plt.ylabel('critical tau')

	plt.figure(1)
	plt.plot(ls_tau, ls_t, 'co', label='')
	plt.xlabel('tau')
	plt.ylabel('t')
	plt.show()


plt.figure(1)
plot_mus(5, 8, 0.001, rescaling=True)
"""
plt.figure(2)
plot_mus(15, 30, 0.001, rescaling=False)
plt.figure(3)
plot_mus(10, 30, 0.001, rescaling=True)
plt.figure(4)
plot_mus(10, 30, 0.001, rescaling=False)
plt.figure(5)
plot_mus(5, 30, 0.001, rescaling=True)
plt.figure(6)
plot_mus(5, 30, 0.001, rescaling=False)
plt.show()"""





"""
[0.10421831976101721, 0.3960247115473133, 0.8500433366680012, 1.4389197827152993, 2.1408744650544613, 2.9394926024010357, 3.8222852707378316, 4.779552876607438, 5.803597428437311, 6.88818265637247, 8.028174833502467, 9.219281670384541, 10.457865138634391, 11.740811478247512, 13.06543061166099, 14.429368599030866, 15.830561001749128, 17.267172149970225, 18.737575155190697, 20.24030312626193, 21.774044656122587, 23.337605154956368, 24.92990182337571, 26.54994683838879, 28.196838899169922, 29.869741905990203, 31.56789306753298, 33.29058824727426, 35.037167827681216, 36.80702560717086, 38.59959948126659, 40.41435544791195, 42.250806795627625, 44.10848823548886, 45.98696532076311, 47.88583588741608, 49.80471232270726, 51.743239898553476, 53.70107524831456, 55.67789476937881, 57.67340020022052, 59.68730055721583, 61.719323046658786, 63.76920665223812, 65.83671031457934, 67.92159727471973, 70.02364502737434, 72.1426391258519, 74.27838227310708, 76.43067891596947, 78.59934474496005, 80.78420279906764, 82.9850822929287, 85.20182813674877, 87.43427466289737, 89.68227319860176, 91.94567247034672, 94.22432529354279, 96.51803254825269]"""


#critical_time_vs_lambda(4, 15 , 100)
#tau_c, nu, lamda = critical_nu(10, 50, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)
#N = 10000
#mus, t_c = mu_evolution(10, 50, 0.001)
#plot_mus(mus, 50,  0.001, t_c, nu)

#tau_c, nu, lamda= critical_nu(10, 35, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)

