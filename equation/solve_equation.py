"""
This module is a collection is tools to resolve a particular 
differential equation, no pretend be more of that or a generalization. 

The equation system to descibre la dynamic of the system is: 
	d(mu)/dt = (k+1)(k+2) mu(k+2) - (k)(k-1) mu(k)
And may be write in matritial format as: 
	mu' = A mu 
where mu' and mu are vector and A is a matrix with coeficients (k+1)(k+2) and k(k-1)

to more information please see: []
"""

import math 
import numpy as np
import matplotlib.pyplot as plt



def poisson_coordenates(lamda, k):
	""" 
	:param int lamda: mean of degree distribution to a poisson distribution.
	:param int k:  ????
	
	:return float: Value of a possion distributio P(lamda, k).
	"""
	return math.exp(-lamda)*lamda**k/math.factorial(k)

def make_vec_poisson(lamda, size):
	"""
	:param int lamda:  mean of degree distribution to a poisson distribution.
	:param int size: size of the array distribution.

	:return list: returnt a list like as poission distribution.
	"""
	return [poisson_coordenates(lamda, k) for k in range(size)]



def emptylist(size):
	"""
	create a empty list
	
	:param int size: longitud of the list. 

	:return list: empty  list with len = `size` 
	"""
	empty_list = []
	for i in range(0, size):
		empty_list.append([])

	return empty_list


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
		print(t_c)
	else:
		t = tau
		t_c = 2

	for i in range(len(mus)):
		
		if i in [0, 1, 2, 3, 4, 5, 10, 15]:
			plt.plot(t, mus[i], label=f'mu(k={i})')
		else:
			plt.plot(t, mus[i])

	plt.vlines(t_c, 0, 0.5, linestyles='dashed', label='critical')

	plt.xlabel('tau')
	plt.ylabel('ratio nodos')
	plt.title('Límite de grafo grande: Distribución de grados en tau.')
	plt.legend()
	plt.show()

def get_critical_time(k, size):
	solution, eige_values, eige_vectors = solve_equation(k, size)
	tau = 0
	dtau = 0.001
	t_c = 0
	nu = 9999
	
	while nu > 1:
		mu = mu_tau(tau, solution, eige_values, eige_vectors)
		nu = nu_tau(mu)
		lamda = function_lambda(mu)
		t_c+= tau2time(lamda, nu, dtau) 
		tau+=dtau
	
	return t_c





#print(get_critical_time(5, 30))
#plot_mus(5, 30, 0.001, rescaling=True)

#critical_time_vs_lambda(4, 15 , 100)
#tau_c, nu, lamda = critical_nu(10, 50, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)
#N = 10000
#mus, t_c = mu_evolution(10, 50, 0.001)
#plot_mus(mus, 50,  0.001, t_c, nu)

#tau_c, nu, lamda= critical_nu(10, 35, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)

