import math 
import numpy as np
import matplotlib.pyplot as plt

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
	for k in range(1, size+1):
		v_poisson.append(poisson_coordenates(lamda,k))

	return v_poisson

def mu_tau(tau, solution, self_value, self_vector):	
	mu = []
	for i in range(len(solution)):
		aux_mu = 0
		for k in range(len(solution)):
			aux_mu += self_vector[i][k] *  solution[k] * np.exp(self_value[k]*tau)
		
		mu.append(aux_mu) 

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

def critical_t(solution, self_values, self_vector):
	tau = 0
	dtau = 0.0001
	t_c = 0
	nu = 100
	while nu > 1:
		mu = mu_tau(tau, solution, self_values, self_vector)
		nu = nu_tau(mu)
		lamda= lamda_tau(mu)
		t_c+= dtau * nu*lamda/math.log(math.exp(1), nu)
		tau+=dtau
	
	return t_c
	#print(integral/np.log(10000) * 10000)
		

def solve_equation(lamda, size):
	M = original_matrix(size) # crea la matriz
	eigen_values, eigen_vectors = np.linalg.eig(M) # devuelve autovalores/vectores
	v_poisson = make_vec_poisson(lamda, size)
	solution = np.linalg.solve(eigen_vectors, v_poisson)
	return critical_t(solution, eigen_values, eigen_vectors)



def critical_time_vs_lambda(lambda_min, lambda_max, size):
	t_c = []
	for i in range(lambda_min, lambda_max):
		t_c.append(solve_equation(i, size))

	plt.figure(1)
	plt.plot(list(range(lambda_min, lambda_max)), t_c, 'ro', label='numerical results')
	plt.legend()
	plt.xlabel('Lambda')
	plt.ylabel('Critical time')
	plt.title('Large graph limit of critical times')
	plt.show()


critical_time_vs_lambda(4, 21, 75)



