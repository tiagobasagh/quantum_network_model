import math 
import numpy as np

def original_matrix(size):
	M = np.zeros((size,size))
	for i in range(size):
		M[i,i] = a_value(i+1)

		if i < size-2:
			M[i,i+2] = b_value(i+1)

	return M

def a_value(k):
	return -k*(k-1)

def b_value(k):
	return (k+1)*(k+2)

def poisson_coordenates(lamda, k):
	return math.exp(-lamda)*lamda**k/math.factorial(k)

def make_vec_poisson(lamda, size):
	v_poisson = []
	for k in range(size):
		v_poisson.append(poisson_coordenates(lamda,k))

	return v_poisson

def mu_tau(tau, solution, self_value, M):	
	vec = solution * np.exp(self_value*tau)
	mu = np.matmul(M, vec)
	return mu

def lamda_tau(mu):
	lamda = 0
	for i in range(len(mu)):
		lamda += i * mu[i]
	return lamda 

def nu_tau(mu):
	lamda = lamda_tau(mu)
	p = 0
	for i in range(len(mu)):
		p += i*(i-1)* mu[i]

	return p/lamda

def integrate_nu(solution, self_values, M):
	integral = 0
	function = []
	inversa = []
	
	for t in range(3):
		mu = mu_tau(t,solution, self_values, M)
		nu = nu_tau(mu)
		lamda = lamda_tau(mu)
		integral += math.log(nu)/(nu*lamda)
		inversa.append( integral**(-1))	
		function.append(integral)

	print(integral)
	print(function)
	print(inversa)

def solve_equation(lamda, size):
	M = original_matrix(size)
	w,v = np.linalg.eig(M)
	v_poisson = make_vec_poisson(lamda, size)
	solution = np.linalg.solve(v, v_poisson)
	integrate_nu(solution, w, v)



solve_equation(10, 10)



