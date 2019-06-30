import math 
import numpy as np

def eigein_value(k):
	return -k*(k-1)

def recursive_value(j,k):
	return (j*(j-1) - k*(k-1))/((j+1)*(j+2))

def normal_mode(k, j_o, size):
	vec =[]
	A = 1 
	
	if j_o == 0: 
		vec.append(0)
		vec.append(1)
		vec.append(0) 
		j = 2	
	else:
		vec.append(1)
		vec.append(0)
		j = 1 
	
	while j+1 < size:
		if j%2==j_o%2 and j<k:
			A *=recursive_value(j, k)
			vec.append(A)
		else:
			vec.append(0)

		j+=1

	return vec


def make_elements(total_normal_modes):
	normal_modes = []
	eigein_values = []
	for k in range(1, total_normal_modes + 1):
		eigein_values.append( eigein_value(k))
		normal_modes.append( normal_mode(k, k%2, total_normal_modes))

	return normal_modes


def build_matrix(l_of_l):
	a = ''
	for i in range(len(l_of_l[0])):
		for j in range(len(l_of_l)):
			if j == len(l_of_l)-1:
				a+= str(l_of_l[j][i])
			else:
				a+= str(l_of_l[j][i]) +','
		if i != len(l_of_l[0])-1:
			a+=';'
	
	return a

def poisson_coordenates(lamda, k):
	return math.exp(-lamda)*lamda**k/math.factorial(k)

def make_v_poisson(lamda, size):
	v_poisson = []
	for k in range(size):
		v_poisson.append(poisson_coordenates(lamda,k))

	return v_poisson


def solve_equation(lamda, size):
	M = np.matrix(build_matrix(make_elements(size)))
	v_poisson = make_v_poisson(lamda, size)
	solution = np.linalg.solve(M, v_poisson)

	return solution

#normal_mode(4, 0, 4)

size = 30
lamda = 10
sol = solve_equation(lamda, size)
print(sol)


