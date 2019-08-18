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

def original_matrix(size):
	"""Build de matrix that describe the diferential equation.

    Parameters
    ==========
    int: size of the matrix.

    Returns
    =======
    np.array:
      return an array 
    """
	M = np.zeros((size, size))
	for i in range(size):
		M[i,i] = a_value(i+1)
		if i < size-2:
			M[i,i+2] = b_value(i+1)

	return M

def a_value(k):
	"""Diagonal coeficient of the matrix. 
	
	Parameters
	==========
	int: k position inside the matrix.

	Returns
	======
	int: diagonal coeficient value 
	"""
	return -k*(k-1)

def b_value(k):
	"""Unique coeficients [k, k+2] non zero outside diagonal. 
		
	Parameters
	==========
	int: K, position inside the matrix.

	Returns
	======
	int: non diagonal coeficient value.
	"""
	return (k+1)*(k+2)

def poisson_coordenates(lamda, k):
	""" 

	Parameters
	==========
	int: lamda, mean of degree distribution to a poisson distribution.
	int: k, ????

	Returns
	======
	float: Value of a possion distributio P(lamda, k).

	"""
	return math.exp(-lamda)*lamda**k/math.factorial(k)


def make_ver_uniform(lamda, size):
	""" 

	Parameters
	==========
	int: lamda, mean of degree distribution to a poisson distribution.
	int: size, size of the array distribution.

	Returns
	======
	list: list of floats, the element j is equal to P(lamda, j)

	"""
	v_poisson = []
	for i in range(0, size):
		if i < lamda:
			v_poisson.append(1/lamda)
		else:
			v_poisson.append(0)

	return v_poisson

def make_vec_poisson(lamda, size):
	""" 

	Parameters
	==========
	int: lamda, mean of degree distribution to a poisson distribution.
	int: size, size of the array distribution.

	Returns
	======
	list: list of floats, the element j is equal to P(lamda, j)

	"""
	v_poisson = []
	for k in range(1, size+1):
		v_poisson.append(poisson_coordenates(lamda,k))

	return v_poisson

def mu_tau(tau, solution, self_value, self_vector):	
	""" 
	calculation of mu(tau)

	Parameters
	==========
	float: tau.
	solution: vector of 
	numpy array: self_value: eigen values of A matrix.
	numpy array: self_vector: eigen vector of A matrix.

	Return
	======
	list: list of mu value to all k in tau time.  

	"""

	mu = []
	for i in range(len(solution)):
		aux_mu = 0
		for k in range(len(solution)):
			aux_mu += self_vector[i][k] *  solution[k] * np.exp(self_value[k]*tau)
		
		mu.append(aux_mu) 

	return mu

def lamda_tau(mu):
	"""
	Calculate lambda value using: 
		lambda = SUM_{i=1}^M mu(i)
	where M is the longitud of mi vector mu.
	
	parameters
	==========
	list of floats: mu: 

	return
	======
	float: 
	"""

	lamda = 0
	for i in range(len(mu)):
		lamda += i * mu[i]
	return lamda 

def nu_tau(mu):
	"""
	Calculate lambda value using: 
		lambda = SUM_{i=1}^M mu(i)
	where M is the longitud of mi vector mu.
	
	parameters
	==========

	return
	======

	"""
	lamda = lamda_tau(mu)
	p = 0
	for i in range(len(mu)):
		p += i*(i-1)* mu[i]

	return p/lamda

def critical_t(solution, self_values, self_vector):
	"""
	
	parameters
	==========

	return
	======

	"""
	tau = 0
	dtau = 0.01
	t_c = 0
	nu = 100
	while nu > 1:
		mu = mu_tau(tau, solution, self_values, self_vector)
		nu = nu_tau(mu)
		lamda= lamda_tau(mu)
		t_c+= dtau * nu*lamda/math.log(math.exp(1), nu)
		tau+=dtau
	
	return t_c
		

def solve_equation(lamda, size):
	"""
	parameters
	==========

	return
	======

	"""
	#v_poisson, size = make_ver_uniform(lamda)
	M = original_matrix(size) # crea la matriz
	eigen_values, eigen_vectors = np.linalg.eig(M) # devuelve autovalores/vectores
	v_poisson = make_vec_poisson(lamda, size)
	
	solution = np.linalg.solve(eigen_vectors, v_poisson)
	
	return solution, eigen_values, eigen_vectors

def empty_list(size):
	"""
	
	parameters
	==========

	return
	======

	"""
	empty_list = []
	for i in range(0, size):
		empty_list.append([])

	return empty_list

def mu_evolution(lamda, size, dtau):
	"""
	parameters
	==========

	return
	======

	"""
	mu_matrix_evolution = empty_list(size)

	solution, self_values, self_vector = solve_equation(lamda, size)
	
	for tau in np.arange(0, 3, dtau):
		mu = mu_tau(tau, solution, self_values, self_vector)
		for i in range(0, size):
			mu_matrix_evolution[i].append(mu[i])

	return mu_matrix_evolution


def critical_nu(k, size, dtau):
	"""
	
	parameters
	==========

	return
	======

	"""
	tau_c = 0
	nu = []
	lamda = []
	found = False
	
	solution, self_values, self_vector = solve_equation(k, size)
	
	for tau in np.arange(0, 3, dtau):
		mu = mu_tau(tau, solution, self_values, self_vector)
		nu.append(nu_tau(mu))
		lamda.append(lamda_tau(mu))
		if nu[int(tau/dtau)] < 1 and not found:
			tau_c = tau
			found = True
	
	return tau_c, nu, lamda

def plot_nu(tau_c, nu, dtau, lamda=[]):
	""".
	parameters
	==========

	return
	======

	"""
	plt.figure(1)
	if lamda:
		plt.plot(np.arange(0, 3, dtau), lamda, label='Lambda(tau)')
			
	plt.plot(np.arange(0, 3, dtau), nu, label='Nu(tau)')
	plt.vlines(tau_c, 0, max(nu), colors='r', linestyles='dashed',  label=f'Critical Tau: {tau_c}')
	plt.legend()
	plt.show()

def plot_mus(mus, number_show, dtau):
	"""
	==========

	return
	======

	"""
	plt.figure(1)
	for i in range(0, number_show):
			plt.plot(list(np.arange(0, 3, dtau)), mus[i], label=f'mu(k={i})')
	plt.legend()
	plt.show()


def critical_time_vs_lambda(lambda_min, lambda_max, size):
	"""
	Calculate lambda value using: 
		lambda = SUM_{i=1}^M mu(i)
	where M is the longitud of mi vector mu.
	
	parameters
	==========

	return
	======

	"""
	t_c = []
	for i in range(lambda_min, lambda_max):
		s, eige_values, eiges_vectors = solve_equation(i, size)
		t_c.append(critical_t(s, eige_values, eiges_vectors))

	plt.figure(1)
	plt.plot(list(range(lambda_min, lambda_max)), t_c, 'ro', label='numerical results')
	plt.legend()
	plt.xlabel('Lambda')
	plt.ylabel('Critical time')
	plt.title('Large graph limit of critical times')
	plt.show()

a, b ,c= solve_equation(10, 30)
print(c)
#critical_time_vs_lambda(4, 20 , 1)
#tau_c, nu, lamda = critical_nu(10, 10, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)
#mus = mu_evolution(10, 30, 0.001)
#plot_mus(mus, 15,  0.001)
#tau_c, nu, lamda= critical_nu(20, 35, 0.001)
#plot_nu(tau_c, nu, 0.001, lamda=lamda)

