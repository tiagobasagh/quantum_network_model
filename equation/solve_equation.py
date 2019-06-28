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

	print(size)
	while j < size:
		print(j)
		print(vec)
		if j <k:
			A *=recursive_value(j, k)
			vec.append(A)
			vec.append(0)
			j+=2
		else:
			vec.append(0)
			j+=1

	return vec

def make_elements(total_normal_modes):
	normal_modes = []
	eigein_values = []
	for k in range(1, total_normal_modes + 1):
		eigein_values.append( eigein_value(k))
		normal_modes.append( normal_mode(k, k%2, total_normal_modes+ 2))

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

ltol = make_elements(4)

print(ltol)
M = np.matrix(build_matrix(ltol))
v_poisson = np.random.poisson(10, 6)


solution = np.linalg.lstsq(M, v_poisson, rcond=None)

print(M)
print(v_poisson)
print(solution[0])
