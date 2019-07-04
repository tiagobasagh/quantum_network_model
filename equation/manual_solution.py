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

def get_eigein_values(total_normal_modes):
	eigein_values = []
	for k in range(1, total_normal_modes + 1):
		eigein_values.append( eigein_value(k))

	return eigein_values

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

def mu_tau():
	def mu_tau(tau, solution, self_value, M):	
	mu = []

	vec = solution * np.exp(self_value*tau)
	mu = np.matmul(M, vec)
	for i in range(len(solution)):
		aux_mu = 0
		for l in range(len(solution)):
			aux_mu += solution[l] * math.exp(self_value[l] *tau) *M[i,l]

		mu.append(aux_mu)
	print(f'WACHHHHHIIIIN {tau}')
	print(mu_2)
	print(mu)
	return mu